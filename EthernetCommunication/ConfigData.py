
class ConfigurationData:
    vehicleSpd = 0
    vehicleAng = 0
    vehicleType = 'S'
    AccelPedlPos = 0
    Transmission = 0
    PowerControlStatus = 0
    IsFailure = 0
    IsSafetyOn = 0

    def update_config(self, param,  val):
        if param == 'Speed':
            self.vehicleSpd = val
        elif param == 'Ang':
            self.vehicleAng = val
        elif param == 'Type':
            self.vehicleType = val
        elif param == 'Acc':
            self.AccelPedlPos = val
        elif param == 'Trm':
            self.Transmission = val
        elif param == 'Pow':
            self.PowerControlStatus = val
        elif param == 'Fal':
            self.IsFailure = val
        elif param == 'Saf':
            self.IsSafetyOn = val





