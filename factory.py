class Reclamo:
    # clase padre de reclamos
    def __init__(self, nombres, ap_paterno, ap_materno, correo, dni, estado, fecha):
        self.nombres = nombres
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.correo = correo
        self.dni = dni
        self.estado = "pendiente"
        self.fecha = fecha
# 


class ServicioReclamo(Reclamo):
    # clase padre de reclamos
    def __init__(self, nombres, ap_paterno, ap_materno, correo, dni, estado, fecha, motivo, detalle, solicitud):
        super().__init__(nombres, ap_paterno, ap_materno, correo, dni, estado, fecha)
        self.motivo = motivo
        self.detalle = detalle
        self.solicitud = solicitud


    def actualizar_estado(self, estado):
        # Actualiza el estado del reclamo.
        self.status = status

    def comprobar_usuario(self, dni):
        if dni:
            return True
        else: False


class AtencionReclamo(Reclamo):
    # clase padre de reclamos
    def __init__(self, nombres, ap_paterno, ap_materno, correo, dni, estado, fecha, msg):
        super().__init__(nombres, ap_paterno, ap_materno, correo, dni, estado, fecha)
        self.msg = msg

    def actualizar_estado(self, estado):
        # Actualiza el estado del reclamo.
        self.status = status
