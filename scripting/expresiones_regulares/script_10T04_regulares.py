import re

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
#patron = "a[a-z]{3}"

#print(re.search(patron, texto))
#print(re.match(patron, texto))
#print(re.findall(patron, texto))
#print(re.search(patron, texto).group())

#print(re.sub(patron, "###", texto))

'''
1) re.search(pattern, string, flags=0)

    - Examina a través de la string («cadena») buscando el primer lugar donde el pattern («patrón») 
        de la expresión regular produce una coincidencia, y retorna un objeto match correspondiente.
        Retorna None si ninguna posición en la cadena coincide con el patrón; notar que esto es 
        diferente a encontrar una coincidencia de longitud cero en algún punto de la cadena.
    - De por sí no devuelve nada. Devuelve 'None' y por eso usamos bool.
    - Busca en todo el texto la primera aparición.

2) re.match(pattern, string, flags=0) 

    - Si cero o más caracteres al principio de la string («cadena») coinciden con el pattern («patrón») 
        de la expresión regular, retorna un objeto match correspondiente. Retorna None si la cadena 
        no coincide con el patrón; notar que esto es diferente de una coincidencia de longitud cero.
    - De por sí no devuelve nada. Devuelve 'None' y por eso usamos bool.

3) re.split(pattern, string, maxsplit=0, flags=0)

    - Divide la string («cadena») por el número de ocurrencias del pattern («patrón»). Si se utilizan 
        paréntesis de captura en pattern, entonces el texto de todos los grupos en el patrón también 
        se retornan como parte de la lista resultante. Si maxsplit (máxima divisibilidad) es distinta
        de cero, como mucho se producen maxsplit divisiones, y el resto de la cadena se retorna como 
        elemento final de la lista.


4) re.findall(pattern, string, flags=0)

    - Retorna todas las coincidencias no superpuestas de pattern en string, como una lista de strings
        o tuplas. El string se escanea de izquierda a derecha y las coincidencias se retornan en el 
        orden en que se encuentran. Las coincidencias vacías se incluyen en el resultado.
    
    - El resultado depende del número de grupos detectados en el patrón. Si no hay grupos, retorna 
        una lista de strings que coincidan con el patrón completo. Si existe exactamente un grupo, 
        retorna una lista de strings que coincidan con ese grupo. Si hay varios grupos presentes, 
        retorna una lista de tuplas de strings que coinciden con los grupos. Los grupos que no son 
        detectados no afectan la forma del resultado.

    - Te va a traer todas las apariciones.

'''