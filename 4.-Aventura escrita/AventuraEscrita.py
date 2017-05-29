# -*- encoding: utf-8 -*-
decision1=decision2=decision3=decision4=decision5=decision6=decision7=decision8=decision9 = ""
nombre = False
print("Aventuras en el plano de Zendikar")
nombre = input ("Cual es tu nombre ")
while nombre == "":
    nombre = input ("Cual es tu nombre ")
print ("hola " +nombre+ " que se encuentra una tarde dentro de una taberna relajado y ansioso porque algo grande pasara, cansado del ambiente rutinario de los habitantes de Zendikar. Un disturbio llama tu atencion y te diriges afuera de la taberna para saber que esta sucediendo.")
print ("Dos personas se encuentran afuera de una taberna peleando en una rinia, rodeado de una multitud indignante, una pelea “aparentemente” dispareja, dos hombres uno aspecto grotesco, corpulento, grandes brazos marcados con cicatrices doblándole la altura al otro individuo, pequeño, delgado e indefenso en apariencia de una edad avanzada, siendo sometido todo el tiempo por su contrincante en turno.")
while decision1 != "si" and decision1 != "no" and decision1 != "No" and decision1 != "Si":
    decision1 = input ("Quieres ayudar al hombre pequeno ")
    if decision1 != "si" and decision1 != "no" and decision1 != "No" and decision1 != "Si":
        print("Esa no es una decision correcta")
if decision1 == "si" or decision1 == "Si":
    print("Te acercas para ayudarlo alzando tu espada y de una patada derribas al imponente opresor, las personas asombradas celebran aquella gran hazaña mientras el hombre derribado, disgusto, se retira entre la multitud. Regresas a estrecharle la mano la pequeña víctima y el gustoso te regresa el saludo, mientras dice: “muchas gracias por la ayuda joven, déjeme agradecerle con este pequeño presente”")
    print ("El anciano te presenta una suma de oro, lo suficientemente hostentosa para mantener una pequeña familia durante algunos años.")
    while decision2 != "si" and decision2 != "no":
        decision2 = input ("Aceptas la suma de dinero si/no ")
    if decision2 == "si":
        print("Aceptas la recompensa como cualquier persona lo haría, valla un saco de oro no se le niega a nadie, te regocijas en oro puro por un momento hasta que entras en razón y le das un buen uso, decides invertirlo en la taberna que solías frecuentar para ser su dueño y durante toda la vida tener un ingreso seguro, sin duda la mejor decisión que creíste haber hecho.")
    if decision2 =="no":
      print("Amablemente te niegas al presente, el anciano impresionado dice: “Sabía que había tomado la mejor decisión en venir hasta acá… joven muchacho te ofrezco una pequeña aventura, estoy convencido de que no será ningún reto para ti.")
      print("El anciano entiende que eres una persona con gran valor y en cambio te ofrece otro desafío, esta vez necesita que lo acompañes a las cavernas cercanas para que lo ayudes a recuperar un artefacto antiguo de gran valor para él.")
      print("En la entrada de las cavernas reposa una esfinge que bloquea la entrada a la caverna. Te ofrece el paso a cambio de que respondas correctamente uno de sus acertijos. Lanzando una pequeña riza ya que sabe que nadie a podido responder uno de sus retos")
      while decision3 != "El hombre" and decision3 != "Hombre" and decision3 != "hombre" and decision3 != "el hombre" and decision3 != "El humano" and decision3 != "el humano" and decision3 != "humano" and decision3 != "Humano":
          decision3 = input("¿Cuál es el que al mismo tiempo es un bípedo, un trípedo y un cuadrúpedo? ")
          if decision3 != "El hombre" and decision3 != "Hombre" and decision3 != "hombre" and decision3 != "el hombre" and decision3 != "El humano" and decision3 != "el humano" and decision3 != "humano" and decision3 != "Humano":
              print ("Esa no es una decision correcta")

      print("La esfinge impresionada por la respuesta desbloquea el paso hacia la cueva, oscura y fría como no la habías imaginado, y les entrega un presente. Frente a ti tienes a escoger un hada o una lampara de aceite.")
      while decision4 != "hada" and decision4 != "lampara" and decision4 != "Hada" and decision4 != "Lampara":
          decision4 = input("que llevaras con tigo?")
          if decision4 != "hada" and decision4 != "lampara" and decision4 != "Hada" and decision4 != "Lampara":
              print("Esa no es una decision correcta")
      if decision4 == "hada" or decision4 == "Hada":
          print("Decides que la hada es la mejor opción para seguir y adentrarte a lo profundo de la caverna. Gracias a la capacidad de la pequeña hada estas seguro dentro de la caverna ya que su luz jamás se apagara. La hada como pequeña ayuda te indica un camino seguro por donde puedes continuar tu camino. Sigues avanzando por la caverna y te encuentras con una encrucijada, dos caminos, aparentemente similares, tu pequeña hada que indica que vallas por el de la derecha, sin embargo ella simplemente te está aconsejando, la decisión es tuya, ir por la derecha o la izquierda.")
          while decision5 != "izquierda" and  decision5 != "derecha" and decision5 != "Izquierda" and decision5 != "Derecha":
              decision5 = input("Que camino tomaras? ")
              if decision5 != "izquierda" and  decision5 != "derecha" and decision5 != "Izquierda" and decision5 != "Derecha":
                  print("Esta no es una decision correcta")
          if decision5 == "Izquierda" or decision5 =="izquierda":
              print("Decides seguir tu instinto y te vas por la izquierda ignorando por completo lo que la pequeña hada te aconsejaba. Caminas por la caverna y comienzas a ver que del techo cuelgan lianas muy grandes y pegajosas por las cuales tienes que pasar apartándolas del camino, tu pequeña hada compañera queda atrapada en una liana, la ayudas, la tomas entre tus brazos y sigues avanzando, ahora sabes porque ella quería el otro camino, era imposible para ella cursar por allí sin ayuda, en cambio tu cruzas junto con ella sin ninguna dificultad.")
              print("En el fondo de la cueva te encuentras con creaturas muy parecidas a caballos con un pelaje color verde que mantienen bajo custodia una reliquia que brilla de color rojo pálido. Tu amigo señala que eso es por lo que han venido y alerta a recuperarlo. ¿Qué harás?")
              while decision6 != "Exigir que te regresen lo que te pertenece" and decision6 != "Salir corriendo" and decision6 != "Negociar":
                  decision6 = input("a)Exigir que te regresen lo que te pertenece \nb)Salir corriendo \nc)Negociar \n")
              if decision6 == "Exigir que te regresen lo que te pertenece":
                  print("Bien dicho, despues de todo es tuyo y te lo mereces. Al aproximarte a el botin eres descubierto, las creaturas son mas fuertes de lo que parecian, de una patada pierdes el conocimiento. Mejor suerte la proxima vez")
              if decision6 == "Salir corriendo":
                  print("Te has salvado de un buen lio, estas creaturas parecian ser verdaderamente salvajes, ahora puedes reflexionar enlo que ha pasado y nunca mas meterte con extraños y sus deseos de avaricia.")
              if decision6 == "Negociar":
                  print("Estas creaturas parecen ser increiblemente inteligentes, aunque no conocen tu lenguage, logran desifrarlo en cuestion de minutos y asi llegan a un acuerdo, parece que te cambiaran lo que deseas a cambio de que informes a la esfinge del deseo de estos animales de querer salir mas a menudo, parece que les a armado un gran lio esa esfinge. Finalmente fuera de la cueva el anciano te revela que es un gran rey y te nombrara caballero de la corte. Felicidades has ganado.")
          if decision5 == "Derecha" or decision5 =="derecha":
              print("Decides seguir el consejo la pequeña hada y tomas el camino de la derecha, continuas por la caverna y comienzas a notar que el terreno es un poco inestable, el suelo parece despedazarse cada vez que das un paso, pero no puedes regresar todo se desmorona detrás de ti, debes de correr por tu vida y salvarte, llevas a salvo hasta un punto donde al parecer el terreno es estable y no corres riesgos de caerte al vacío, la hada, al poder volar, no le pareció problemático ese camino ya que jamás ha puesto un pie en el suelo. La pequeña carrera te deja exhausto y asustado.")
              print("Una vez que recuperas el aliento encuentras rio que ve cuesta abajo, dado que tu camino de vuelta a sido destrosado mientras avanzabas ahora tu unica opcion es bajar. Mirando mas detenidamente notas que en la parte mas baja hay un tesoro, custodiado por un fauno ambriento y lo que parece ser una salida, tus opciones son salir de la cueva o negociar con el fauno.")
              while decision6 != "negociar" and decision6 != "escapar" and decision6 != "Escapar" and decision6 != "Negociar":
                  decision6 = input("Negociar\nCorrer\n")
                  if decision6 != "negociar" and decision6 != "escapar" and decision6 != "Escapar" and decision6 != "Negociar":
                      print ("Esa no es una respuesta valida")
              if decision6 == "Negociar" or decision6 == "negociar":
                  print("El fauno parece no estar muy interesado en el tesoro que se encuentra a sus pies, dice que lo puedes tomar pero que acambio le permitas quedarte con el hada que llevas con tigo, el hada accede y se despide de ti con lagrimas en los ojos, despues de todo parece que le empezabas a agradar, ahora estas por tu cuenta y tienes un botion enorme, el mundo es tuyo.")
              if decision6 == "Escapar" or decision6 == "escapar":
                  print("Sales sano y salva de la cueva, tu nuevo amigo parece no estar muy contento, despues de todo no encontraron eso por lo que venian, y la pequeña hada parece habarte agarrado algo de afecto, al final del dia ganaste un nuevo amigo. Felicidades.")
      if decision4 == "Lampara" or decision4 == "lampara":
          print("Decides que la tecnología humana es mejor para dicha labor así que tomas la linterna y prosigues tu camino en la oscura caverna. Aunque vez perfectamente en la oscuridad no tienes idea de a donde tienes que ir pero tú sigues moviéndote por tu instinto y todo parece marchar bien, pero tienes que darte prisa ya que la linterna no es eterna y puedes quedarte sin combustible y perderte para siempre en la oscuridad. Al llegar a un espacio grande y amplio de la caverna una criatura detecta tu presencia y decide atacarte, tu mente piensa, puedo lanzarle algo de petróleo encima con mi linterna y con una pequeña chispa puedo prenderle fuego y matarlo, pero al mismo tiempo gastarías una parte de lo que te queda de combustible para ver en la oscuridad…por lo cual correr a toda marcha también es una opción que cruza por tu cabeza")
          while decision5 != "Quemarlo" and decision5 != "Correr":
              decision5 = input("Quemarlo\nCorrer\n")
      if decision5 == "Quemarlo" or decision5 == "quemarlo":
          print("Tu mente de hombre cazador te hace seguir el camino de la sangre y enfrentarte con la criatura misteriosa, aun sabiendo los riesgos que esto conlleva. Maniobras audaz mente y logras vaciarle petróleo enzima  y con una pequeña chispa de tu ingenio… la criatura arde en fuego rápidamente y es consumida por el mismo hasta quedarse inmóvil en el piso, lamentablemente uno de tus brazos se ve alcanzado por las llamas lo cual te deja un enorme dolor y en una marca permanente. Te quedas frustrado por el dolor mientras te percatas que dentro de esta criatura emite una pequeña luz, te acercas lentamente y efectivamente, una gema de luz brillante yace en su interior, metes la mano dentro la criatura lo cual te causa repulsión pero igual lo haces, cuando la tomas la voz del anciano suena en tu mente y dice “por fin has encontrado la “Gema de la Zendikar” esa gema posee propiedades regenerativas que a cualquiera que la posea será liberado de cualquier enfermedad o dolor que sienta en su cuerpo, esa criatura lo posea por eso podía vivir en tan extremas circunstancias, puedes conservarla ya que ahora descanso en saber que está en manos de alguien digno de ella…” De pronto tu cuerpo lentamente comienza a regenerarse mientras te das cuenta de que el techo se viene abajo y colapsa sobre ti. Al recobrar la conciencia estas ileso debajo de unas cuentas rocas la luz yace sobre el horizonte y con tu nueva adquisición te sientes mejor que nunca para conseguir nuevas aventuras y quien sabe cuántas gemas poderosas pueda haber por allí.")
      if decision5 == "Correr" or decision5== "correr":
          print("Decides que nada bueno saldrá de enfrentar a esta bestia desconocida y sales corriendo para salvar tu vida, corres y corres mientras el fuego de tu linterna se apaga y te quedas completamente ciego en la oscuridad, la bestia dejo de seguirte casi al mismo tiempo en que saliste corriendo, le importas demasiado poco como para ir detrás de ti. Desesperadamente intentas prender la antorcha de nuevo pero en la completa oscuridad es una tarea difícil, tras unas cuantas horas de intentarlo lo logras, pero el combustible de la linterna no te duraría mucho… vagas por la caverna sin rumbo alguno, completamente perdido, hasta que por fin… la luz de tu linterna se extingue para siempre… sin saber la diferencia entre tener los ojos cerrados o abiertos el pánico invade tu mente y comienzas a caminar a ciegas… callándote, golpeándote, lastimándote una y otra vez sin ni siquiera poder ver tu brazo delante de ti… quedas condenado a una muerte lenta y solitaria en aquella caverna sin fin… una voz en tu mente dice “Ahora no pareces ser digno de dicha aventura y tu fracaso solo lo confirma” tu muerte ha sido tallada y no existe nada más que puedas hacer.")
if decision1 == "no":
    print("Miras con indiferencia hacia donde se encuentra el percance… suspiras y piensas que una vez más la vida insignificante como es no vale la pena ensuciarse las manos y te retiras del lugar. Una vida pacifica sin emociones y con tranquilidad te esperaron toda tu vida y seguiste el camino que siempre creíste mejor, así hasta llegar a la vejes. Puede decirse que viviste como quisiste.")
