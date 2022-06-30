(define (problem carga-aerea)
    (:domain aviones)
    (:objects 
        LA01
        LA02
        LA03
        AA01
        AA02
        AA03
        FB01
        FB02
        FB03
        MDZ
        AEP
        COR
        SFN
        FERTILIZANTE
        TELA-GRANIZO
        COSECHADORA
        AUTOPARTES
        PASAJEROS-HACIA-MDZ
        PASAJEROS-HACIA-SFN
        AVIOCENTRO-SERVICIOS-DE-AVIACION

    )
    (:init 

        (avion LA01)
        (avion LA02)
        (avion LA03)
        (avion AA01)
        (avion AA02)
        (avion AA03)
        (avion FB01)
        (avion FB02)
        (avion FB03)
        (aeropuerto MDZ)
        (aeropuerto AEP)
        (aeropuerto COR)
        (aeropuerto SFN)
        (taller AVIOCENTRO-SERVICIOS-DE-AVIACION)
        (carga FERTILIZANTE)
        (carga TELA-GRANIZO)
        (carga COSECHADORA)
        (carga AUTOPARTES)
        (pasajeros PASAJEROS-HACIA-MDZ)
        (pasajeros PASAJEROS-HACIA-SFN)

        (en LA01 MDZ)
        (en LA02 AEP)
        (en LA03 COR)
        (en AA01 SFN)
        (en AA02 MDZ)
        (en AA03 AEP)
        (en FB01 COR)
        (en FB02 AEP)
        (en FB03 SFN)
        (en FERTILIZANTE AEP)
        (en TELA-GRANIZO SFN)
        (en COSECHADORA MDZ)
        (en AUTOPARTES COR)
        (en PASAJEROS-HACIA-MDZ AEP)
        (en PASAJEROS-HACIA-SFN COR)
    )
    (:goal 
        (and
            (en FERTILIZANTE SFN)
            (en TELA-GRANIZO MDZ)
            (en COSECHADORA COR)
            (en AUTOPARTES AEP)
            (en PASAJEROS-HACIA-MDZ MDZ)
            (en PASAJEROS-HACIA-SFN SFN)
            (en LA01 AVIOCENTRO-SERVICIOS-DE-AVIACION)

        )
    )
)