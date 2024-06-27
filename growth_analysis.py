import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

# Read and visualize growth data
def visualize_growth_curve(file_path):
    # Read data
    data = pd.read_csv(file_path)
    
    # Plot all columns in the same figure
    fig, ax = plt.subplots(figsize=(12, 6))
    for col in data.columns:
        ax.plot(data.index, data[col], label=col)
    ax.legend()
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Growth Curves')
    plt.tight_layout()
    plt.show()

# Analyze growth rate using SVR
def analyze_growth_rate(data):
    X = data.iloc[:, 1].values.reshape(-1, 1)  # Time
    y = data.iloc[:, 0].values.reshape(-1, 1)  # OD or growth value
    
    # Scale data
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X_scaled = sc_X.fit_transform(X)
    y_scaled = sc_y.fit_transform(y)
    
    # Train SVR model
    regressor = SVR(kernel='linear')
    regressor.fit(X_scaled, y_scaled)
    
    # Visualize SVR results
    plt.figure(figsize=(12, 6))
    plt.scatter(sc_X.inverse_transform(X_scaled), sc_y.inverse_transform(y_scaled), color='red', label='Data Points')
    plt.plot(sc_X.inverse_transform(X_scaled), sc_y.inverse_transform(regressor.predict(X_scaled)), color='blue', label='SVR Prediction')
    plt.title('Growth Rate Analysis')
    plt.xlabel('Time')
    plt.ylabel('OD')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Output coefficients
    coefficients = regressor.coef_
    print(f"Coefficients (SVR): {coefficients}")

# Example usage:
if __name__ == "__main__":
    file_path = 'file.csv'  # Replace with your data file path
    visualize_growth_curve(file_path)
    
    # Load data for SVR analysis
    data = pd.read_csv(file_path)
    analyze_growth_rate(data)
