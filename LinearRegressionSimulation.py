import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters as requested
N = 1000  # One thousand point pairs
K = 100   # One hundred trials of a and b

def step1_generate_random_points(n_points):
    """
    Step 1: Generate n_points pairs of random points
    Each point is a 2D vector (x,y) normalized between 0 and 1
    X is independent variable, Y is dependent variable
    Save data in matrix
    """
    x_points = []
    y_points = []
    
    # Generate points one by one
    for i in range(n_points):
        x = random.random()  # Random value between 0 and 1
        y = random.random()  # Random value between 0 and 1
        x_points.append(x)
        y_points.append(y)
    
    # Create matrix to store the data
    data_matrix = []
    for i in range(n_points):
        pair = [x_points[i], y_points[i]]  # Point pair
        data_matrix.append(pair)
    
    return x_points, y_points, data_matrix

def step2_display_points(x_points, y_points):
    """
    Step 2: Display the points on axes
    """
    plt.figure(figsize=(10, 8))
    plt.scatter(x_points, y_points, alpha=0.6, s=15, color='blue')
    plt.xlabel('X (independent variable)')
    plt.ylabel('Y (dependent variable)')
    plt.title(f'{N} Random Points')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

def step3_trial_and_error(x_points, y_points, data_matrix, k_trials):
    """
    Step 3: Trial and error - randomly guess/generate a and b
    Use equation y = a*x + b to go through table/matrix value by value
    Insert into equation with first a and b, find average error of all thousand point pairs
    Do this - randomly generate a and b one hundred times
    N samples - in this case = thousand
    K how many draws of a b = 100 experiments
    """
    all_trials = []
    
    # Perform K trials
    for trial_num in range(k_trials):
        # Randomly draw a and b
        a = random.uniform(-2, 2)  # Draw coefficient a
        b = random.uniform(-1, 2)  # Draw coefficient b
        
        # Go through all points in matrix/table
        total_error = 0
        errors_list = []
        
        for i in range(len(data_matrix)):
            # Extract x and y values from matrix
            x_val = data_matrix[i][0]
            y_actual = data_matrix[i][1]
            
            # Insert into equation y = a*x + b
            y_predicted = a * x_val + b
            
            # Calculate error for this point
            error = abs(y_actual - y_predicted)
            errors_list.append(error)
            total_error += error
        
        # Calculate average error for all thousand points
        average_error = total_error / len(data_matrix)
        
        # Save trial results
        trial_result = {
            'trial_number': trial_num + 1,
            'a': a,
            'b': b,
            'average_error': average_error,
            'all_errors': errors_list
        }
        all_trials.append(trial_result)
    
    return all_trials

def step4_find_best_line(all_trials, x_points, y_points):
    """
    Step 4: Find from all 100 averages the line that produced minimal error
    Add it to the axes with the points
    """
    # Find trial with smallest error
    best_trial = all_trials[0]  # Start with first trial
    
    for trial in all_trials:
        if trial['average_error'] < best_trial['average_error']:
            best_trial = trial
    
    # Display graph with points and best line
    plt.figure(figsize=(12, 8))
    
    # Display all points
    plt.scatter(x_points, y_points, alpha=0.6, s=20, color='blue', label='Original Points')
    
    # Create best line
    x_line = [0, 1]  # From 0 to 1
    y_line = []
    for x in x_line:
        y = best_trial['a'] * x + best_trial['b']
        y_line.append(y)
    
    plt.plot(x_line, y_line, color='red', linewidth=3, 
             label=f'Best Line: y = {best_trial["a"]:.4f}x + {best_trial["b"]:.4f}')
    
    plt.xlabel('X (independent variable)')
    plt.ylabel('Y (dependent variable)')
    plt.title(f'Trial and Error Results: {N} points, {K} trials\nMinimal Error: {best_trial["average_error"]:.6f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1)
    plt.ylim(-0.5, 2)  # Expand to see the line
    
    plt.tight_layout()
    plt.show()
    
    return best_trial

def display_results(all_trials, best_trial, top_n=5):
    """
    Display summary of results
    """
    print("=== TRIAL AND ERROR LINE FITTING RESULTS ===")
    print(f"Parameters: N={N} points, K={K} trials")
    print()
    
    # Best result
    print("=== BEST LINE ===")
    print(f"Trial number: {best_trial['trial_number']}")
    print(f"a (slope): {best_trial['a']:.6f}")
    print(f"b (intercept): {best_trial['b']:.6f}")
    print(f"Equation: y = {best_trial['a']:.6f} * x + {best_trial['b']:.6f}")
    print(f"Minimal average error: {best_trial['average_error']:.6f}")
    print()
    
    # General statistics
    all_errors = [trial['average_error'] for trial in all_trials]
    print("General Statistics:")
    print(f"Smallest error: {min(all_errors):.6f}")
    print(f"Largest error: {max(all_errors):.6f}")
    print(f"Average error of all trials: {sum(all_errors)/len(all_errors):.6f}")
    print()
    
    # Top results
    print(f"=== TOP {top_n} RESULTS ===")
    sorted_trials = sorted(all_trials, key=lambda x: x['average_error'])
    
    for i in range(min(top_n, len(sorted_trials))):
        trial = sorted_trials[i]
        print(f"{i+1}. Trial {trial['trial_number']}: "
              f"a={trial['a']:.4f}, b={trial['b']:.4f}, "
              f"error={trial['average_error']:.6f}")

def main():
    """
    Main function that runs the entire process
    """
    # Step 1: Generate random points and save in matrix
    x_points, y_points, data_matrix = step1_generate_random_points(N)
    
    # Step 2: Display points on graph
    step2_display_points(x_points, y_points)
    
    # Step 3: Trial and error - draw a and b and check errors
    all_trials = step3_trial_and_error(x_points, y_points, data_matrix, K)
    
    # Step 4: Find best line and display it
    best_trial = step4_find_best_line(all_trials, x_points, y_points)
    
    # Display summary
    display_results(all_trials, best_trial)
    
    return data_matrix, all_trials, best_trial

# Run the program
if __name__ == "__main__":
    results = main()