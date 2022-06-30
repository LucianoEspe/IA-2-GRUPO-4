(define (domain aviones)
(:requirements :strips)
(:predicates
	(en ?a ?b) 
	(avion ?a)
	(carga ?c)
	(aeropuerto ?a)
	(pasajeros ?p)
	(taller ?t)

) 
(:action cargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?ap) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?a) 
		(not (en ?c ?ap))
	)
)
(:action descargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?a) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?ap) 
		(not (en ?c ?a))
	)
)
(:action volar
 :parameters ( ?a ?origen ?destino)
 :precondition
	(and (en ?a ?origen) (avion ?a) (aeropuerto ?origen) (aeropuerto ?destino))
 :effect
	(and 
		(en ?a ?destino) 
		(not (en ?a ?origen))
	)
)

(:action volar_al_taller
 :parameters ( ?a ?origen ?t)
 :precondition
	(and (en ?a ?origen) (avion ?a) (aeropuerto ?origen) (taller ?t))
 :effect
	(and 
		(en ?a ?t) 
		(not (en ?a ?origen))
	)
)

(:action subir_pasajeros
 :parameters ( ?p ?a ?ap)
 :precondition
	(and (en ?p ?ap) (en ?a ?ap) (pasajeros ?p) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?p ?a) 
		(not (en ?p ?ap))
	)
)
(:action bajar_pasajeros
 :parameters ( ?p ?a ?ap)
 :precondition
	(and (en ?p ?a) (en ?a ?ap) (pasajeros ?p) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?p ?ap) 
		(not (en ?p ?a))
	)
)
)
