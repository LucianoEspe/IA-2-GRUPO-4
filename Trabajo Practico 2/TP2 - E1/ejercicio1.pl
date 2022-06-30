verificar(valvula_seguridad):-
    estado(valvula_seguridad,ok),writeln('Todo OK').
verificar(valvula_seguridad):-
    estado(valvula_seguridad,desconocido),verificar(espesor_umbral),
    verificar(piloto),verificar(fuga_prevenible),verificar(fuga_fijada).

/*  RAMA IZQUIERDA  */
verificar(espesor_umbral):-
    estado(espesor_umbral,ok),writeln('Espesor OK').
verificar(espesor_umbral):-
    estado(espesor_umbral,desconocido),
    ((estado(oxido_valvula,no),writeln('Verificar el espesor de la valvula, canios y juntas'));
    verificar(oxido_valvula)).
verificar(oxido_valvula):-
    estado(oxido_valvula,desconocido),writeln('Verificar oxido en la valvula de seguridad').

/*  RAMA CENTRAL (NO)*/
verificar(piloto) :- 
    estado(piloto, ok), writeln('Piloto OK').
verificar(piloto) :- 
                estado(piloto, desconocido), 
                ((estado(correcta_prevencion_fuga_sit_orifice, si), writeln('Verificar piloto'));
                verificar(correcta_prevencion_fuga_sit_orifice)).
verificar(correcta_prevencion_fuga_sit_orifice) :- 
                estado(correcta_prevencion_fuga_sit_orifice, desconocido), 
                ((estado(resorte_valvula_seguridad, si), writeln('Verificar si existe una prevención de fugas adecuada entre el asiento y el orificio')); 
                verificar(resorte_valvula_seguridad)).
verificar(resorte_valvula_seguridad) :- 
                estado(resorte_valvula_seguridad, desconocido), 
                ((estado(sensores_valvula_control_bloqueados, no), writeln('Verificar el resorte de seguridad de la valvula')); 
                verificar(sensores_valvula_control_bloqueados)).
verificar(sensores_valvula_control_bloqueados) :- 
                estado(sensores_valvula_control_bloqueados, desconocido), 
                ((estado(estado_valvula_cerrado, no), writeln('Verificar que los sensores de la valvula de control esten bloqueados')); 
                verificar(estado_valvula_cerrado)).
                
verificar(estado_valvula_cerrado) :- 
                estado(estado_valvula_cerrado, desconocido),
                ((estado(valvula_alivio_ok_10_mas_presion, no), writeln('Verificar que la valvula este cerrada'));
                verificar(valvula_alivio_ok_10_mas_presion)).
                
verificar(valvula_alivio_ok_10_mas_presion) :- 
                estado(valvula_alivio_ok_10_mas_presion, desconocido),
                ((estado(valvula_seguridad_evacuacion_continua, no), writeln('Verificar si la valvula de alivio funciona correctamente con un aumento de presion del 10% mas que la presion de regulacion')); 
                verificar(valvula_seguridad_evacuacion_continua)).
verificar(valvula_seguridad_evacuacion_continua) :- 
                estado(valvula_seguridad_evacuacion_continua, desconocido), 
                writeln('Verificar si la valvula de seguridad tiene evacuacion continua').
verificar(valvula_seguridad_evacuacion_continua) :- 
    estado(valvula_seguridad_evacuacion_continua, si).

/*  RAMA CENTRAL (SI)*/
verificar(fuga_prevenible):-
    estado(fuga_prevenible,ok),writeln('Fuga asiento y orificio OK').
verificar(fuga_prevenible):-
    estado(fuga_prevenible,desconocido),
    ((estado(resorte_seguridad_efectivo,si),writeln('Verificar si existe una fuga prevenible entre el asiento y el orificio'));
    verificar(resorte_seguridad_efectivo)).
verificar(resorte_seguridad_efectivo):-
    estado(resorte_seguridad_efectivo,desconocido),
    ((estado(sensor_presion_control_bloqueado,si),writeln('Verificar si el resorte de seguridad es efectivo'));
    verificar(sensor_presion_control_bloqueado)).
verificar(sensor_presion_control_bloqueado):-
    estado(sensor_presion_control_bloqueado,desconocido),
    ((estado(presion_gas,si),writeln('Verificar si los tubos del sensor de presión y de control esta bloqueados'));
    verificar(presion_gas)).
verificar(presion_gas):-
    estado(presion_gas,desconocido),
    ((estado(valvula_seguridad_evacuacion_continua,si),writeln('Verificar si la presion de gas en la linea es apropiada'));
    verificar(valvula_seguridad_evacuacion_continua)).
verificar(valvula_seguridad_evacuacion_continua) :- 
    estado(valvula_seguridad_evacuacion_continua, no).

/*  RAMA DERECHA  */
verificar(fuga_fijada):-
    estado(fuga_fijada,ok),writeln('Fugas OK').
verificar(fuga_fijada):-
    estado(fuga_fijada,desconocido),
    ((estado(fuga_en_junta,si),writeln('Verificar si se arreglo la fuga en la junta'));
    verificar(fuga_en_junta)).
verificar(fuga_en_junta):-
    estado(fuga_en_junta,desconocido),writeln('Verificar fugas en las juntas').


estado(valvula_seguridad,desconocido).                      /* COMPROBAR CONTROL DE VALVULA DE SEGURIDAD (OK-DESCONOCIDO) */

estado(oxido_valvula,desconocido).                          /* OXIDO EN EL CUERPO DE LA VALVULA, CAÑERIAS Y JUNTAS (NO-DESCONOCIDO) */
estado(espesor_umbral,desconocido).                         /* ESPESOR MENOR QUE EL LIMITE DE UMBRAL (OK-DESCONOCIDO) */

estado(piloto, desconocido).                                /* FUNCIONA BIEN EL PILOTO (OK-DESCONOCIDO) */
estado(correcta_prevencion_fuga_sit_orifice, desconocido).  /* HAY UNA CORRECTA PREVENCION DE FUGAS ENTRE SIT Y ORIFICE (SI-DESCONOCIDO) */
estado(resorte_valvula_seguridad, desconocido).             /* ES BUENA LA PERFORMANCE Y EFICIENCIA DEL RESORTE DE SEGURIDAD (SI-DESCONOCIDO) */
estado(sensores_valvula_control_bloqueados, desconocido).   /* SENSORES DE LA VALVULA DE CONTROL CERRADOS (NO-DESCONOCIDO) */
estado(estado_valvula_cerrado, desconocido).                /* EL ESTADO DE LA VALVULA DE CONTROL ESTA EN "CERRADO" (NO-DESCONOCIDO) */
estado(valvula_alivio_ok_10_mas_presion, desconocido).      /* PUEDE FUNCIONAR LA VALVULA DE ALIVIO CON UN 10% MAS DE PRESION (NO-DESCONOCIDO) */
estado(valvula_seguridad_evacuacion_continua, desconocido). /* LA VALVULA DE SEGURIDAD TIENE EVACUACION DE GAS CONTINUA (SI-NO-DESCONOCIDO) */

estado(fuga_prevenible,desconocido).                        /* HAY UNA FUGA PREVENIBLE ENTRE SIT Y ORIFICE (OK-DESCONOCIDO) */
estado(resorte_seguridad_efectivo,desconocido).             /* ES EFECTIVO EL RESORTE DE SEGURIDAD (SI-DESCONOCIDO) */
estado(sensor_presion_control_bloqueado,desconocido).       /* ESTAN OBSTRUIDOS LOS TUBOS DEL SENSOR DE PRESION Y DE CONTROL (SI-DESCONOCIDO) */
estado(presion_gas,desconocido).                            /* ES APROPIADA LA PRESION DE GAS EN LA LINEA (SI-DESCONOCIDO) */

estado(fuga_fijada,desconocido).                            /* ESTA FIJADA LA FUGA EN LAS JUNTAS (OK-DESCONOCIDO) */
estado(fuga_en_junta,desconocido).                          /* HAY UNA FUGA EN LA JUNTA (SI-DESCONOCIDO) */