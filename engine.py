class DieselEngine:
    def __init__(self, ratedpower, fuel_type, max_rpm):
        """
        Initialize the engine with its basic parameters.

        Args:
            displacement (float): Engine displacement in liters.
            fuel_efficiency (float): Base fuel efficiency in liters per hour (L/h).
            fuel_type (str): Type of fuel used (e.g., 'diesel', 'gasoline').
            max_rpm (int): Maximum RPM the engine can achieve.
        """
        self.ratedpower = ratedpower
        self.fuel_type = fuel_type
        self.max_rpm = max_rpm

    def calculate_power(self, rpm):
        """
        Calculate the power output of the engine based on the current RPM.

        Args:
            rpm (int): Engine RPM.

        Returns:
            power (float): Power output in kilowatts (kW).
        """
        if rpm > self.max_rpm:
            rpm = self.max_rpm  # Ensure RPM doesn't exceed the engine's max RPM

        # Simple equation for power output: P = displacement * (rpm / 1000)
        # You could replace this with a more realistic engine equation
        power = self.displacement * (rpm / 1000.0) * 10  # kW
        
        return power
    
    def fuel_efficiency(self, power_req, nengines):
        """
    Calculate the fuel efficiency for a specific power requirement based on engine load.

    Args:
        power_req (float): The total power required by the vessel (in W).
        ratedpower (float): The rated power output of a single engine (in W).
        nengines (int): The number of engines available to meet the power requirement.

    Returns:
        float: Specific Fuel Oil Consumption (SFOC) value, representing the relative fuel consumption rate
               based on engine load. This is calculated using a quadratic function where engine load
               affects the efficiency.
        """
        engine_load = power_req / (self.ratedpower * nengines)

        SFOC= 0.455 * (engine_load)^2 - (0.71 * engine_load) + 1.28

        return SFOC

    def engine_status(self, power_req):
        """
        Returns the engine's current status: power output and fuel consumption.

        Args:
            rpm (int): Current RPM of the engine.

        Returns:
            dict: A dictionary with 'power' and 'fuel_consumption'.
        """
        power_output = power_req
        fuel_consumption = self.fuel_efficiency(power_output) * power_req
        
        return {
            "power_output (kW)": power_output,
            "fuel_consumption (L/h)": fuel_consumption
        }