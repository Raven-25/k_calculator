# Function to get user input for the later calculations 
def get_substance_info():
    substances_info = {}

    # Asking the user what the name, concentration, and coefficient of each reactant / product is. 
    while True:
        substance = input("Enter substance name (type 'done' to finish): ")
        if substance.lower() == 'done':
            break
        try:
            coefficient = int(input(f"Enter the coefficient for {substance}: "))
            concentration = float(input(f"Enter the concentration for {substance} (mol/L) (M): "))
            substances_info[substance] = {'coefficient': coefficient, 'concentration': concentration}
        except ValueError:
            print("Invalid input. Please enter numerical values for coefficient and concentration.")
    return substances_info

# Fuction to calculate K eq
def calculate_equilibrium_constant(reactants, products):
    # Calculate the equilibrium constant K.

    # Calculate product of reactants 
    products_value = 1
    for info in products.values():
        products_value *= info['concentration'] ** info['coefficient']

    # Calculate product of products 
    reactants_value = 1
    for info in reactants.values():
        reactants_value *= info['concentration'] ** info['coefficient']
    
    return products_value / reactants_value

# Function to allow for seamless integration into any program - simply call this function .
def main():
    print("Enter information for reactants:")
    reactants = get_substance_info()
    
    print("\nEnter information for products:")
    products = get_substance_info()
    
    K = calculate_equilibrium_constant(reactants, products)
    print(f"\nThe equilibrium constant K is: {K}")
