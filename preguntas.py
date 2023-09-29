import flet as ft

# Definición de preguntas y respuestas para el personaje A
preguntas_A = {
    0: {
        "texto": "¿Cómo abordaría cada candidato el problema de la educación en el país?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, propongo una mayor inversión estatal en la educación para garantizar la igualdad de oportunidades.",
            "boton2": "Mi enfoque para abordar el problema de la educación en el país se basa en la libertad de elección y la competencia. En un futuro, promoveré un sistema de vouchers que permita a los padres elegir la mejor opción educativa para sus hijos. Esto fomentará la competencia entre las escuelas y mejorará la calidad de la educación. Además, reduciré la burocracia en el sistema educativo y empoderaré a los docentes para que puedan innovar y enseñar de manera efectiva.",
            "boton1": "Creo que es importante abordar el problema de la educación en el país mediante reformas significativas. Estoy dispuesto a considerar diversas opciones, incluido un sistema de vouchers, para mejorar la educación. Sin embargo, también debemos garantizar que se mantenga un estándar de calidad en todas las escuelas y que ningún estudiante se quede atrás. Trabajaré en colaboración con expertos y partes interesadas para encontrar la mejor solución para nuestro sistema educativo.",
            "boton0": "Abogaré por mantener el sistema educativo actual sin cambios significativos. Si bien reconozco que existen desafíos en la educación, no estoy a favor de implementar un sistema de vouchers o introducir cambios drásticos en el sistema. En su lugar, enfocaré mis esfuerzos en mejorar la calidad de las escuelas existentes y brindar más recursos a la educación pública. Creo que el sistema actual puede funcionar mejor con una inversión adecuada y una gestión más eficiente."
        },
        "respuestas_Bullrich": {
            "refute": "Yo, Bullrich, considero que la regulación debe ser flexible para adaptarse a las necesidades locales.",
            "boton2": "Mi enfoque para abordar el problema de la educación en el país se basa en la libertad de elección y la competencia. En un futuro, promoveré un sistema de vouchers que permita a los padres elegir la mejor opción educativa para sus hijos. Esto fomentará la competencia entre las escuelas y mejorará la calidad de la educación. Además, reduciré la burocracia en el sistema educativo y empoderaré a los docentes para que puedan innovar y enseñar de manera efectiva.",
            "boton1": "Creo que es importante abordar el problema de la educación en el país mediante reformas significativas. Estoy dispuesto a considerar diversas opciones, incluido un sistema de vouchers, para mejorar la educación. Sin embargo, también debemos garantizar que se mantenga un estándar de calidad en todas las escuelas y que ningún estudiante se quede atrás. Trabajaré en colaboración con expertos y partes interesadas para encontrar la mejor solución para nuestro sistema educativo.",
            "boton0": "Abogaré por mantener el sistema educativo actual sin cambios significativos. Si bien reconozco que existen desafíos en la educación, no estoy a favor de implementar un sistema de vouchers o introducir cambios drásticos en el sistema. En su lugar, enfocaré mis esfuerzos en mejorar la calidad de las escuelas existentes y brindar más recursos a la educación pública. Creo que el sistema actual puede funcionar mejor con una inversión adecuada y una gestión más eficiente."
        }
    },
    1: {
    "texto": "¿Cuál es la propuesta de cada candidato para mejorar la economía y crear empleos?",
    "respuestas_Massa": {
        "refute": "Yo, Massa, propongo un aumento de impuestos a los más ricos para financiar programas de empleo y protección social.",
        "boton2": "Mi propuesta para mejorar la economía y crear empleos se basa en la dolarización de nuestra economía y la reducción significativa de impuestos. Dolarizar la economía traerá estabilidad y confianza a los inversores, lo que a su vez fomentará la inversión y el crecimiento económico. Además, reduciré drásticamente la carga impositiva sobre las empresas y los individuos, lo que incentivará la inversión y la creación de empleos en nuestro país.",
        "boton1": "Reconozco la importancia de abordar los problemas económicos y la creación de empleo, pero creo que debemos ser cautelosos al implementar cambios drásticos como la dolarización. Estoy dispuesto a considerar propuestas de reducción de impuestos y reformas económicas, pero también debemos garantizar la estabilidad económica y social durante cualquier transición. Trabajaré en conjunto con expertos económicos para encontrar un equilibrio entre las reformas necesarias y la estabilidad.",
        "boton0": "No estoy de acuerdo con la dolarización de la economía ni con la eliminación masiva de impuestos. Creo que estas medidas podrían ser arriesgadas y causar incertidumbre económica. En lugar de eso, buscaré otras formas de estimular la economía y crear empleos, como la inversión en infraestructura y la promoción del comercio internacional. También buscaremos formas de mejorar la economía sin poner en riesgo la estabilidad financiera de nuestro país."
    },
    "respuestas_Bullrich": {
        "refute": "Yo, Bullrich, promoveré la inversión privada y la simplificación de regulaciones para estimular la creación de empleo y el crecimiento económico.",
        "boton2": "Mi propuesta para mejorar la economía y crear empleos se basa en la dolarización de nuestra economía y la reducción significativa de impuestos. Dolarizar la economía traerá estabilidad y confianza a los inversores, lo que a su vez fomentará la inversión y el crecimiento económico. Además, reduciré drásticamente la carga impositiva sobre las empresas y los individuos, lo que incentivará la inversión y la creación de empleos en nuestro país.",
        "boton1": "Reconozco la importancia de abordar los problemas económicos y la creación de empleo, pero creo que debemos ser cautelosos al implementar cambios drásticos como la dolarización. Estoy dispuesto a considerar propuestas de reducción de impuestos y reformas económicas, pero también debemos garantizar la estabilidad económica y social durante cualquier transición. Trabajaré en conjunto con expertos económicos para encontrar un equilibrio entre las reformas necesarias y la estabilidad.",
        "boton0": "No estoy de acuerdo con la dolarización de la economía ni con la eliminación masiva de impuestos. Creo que estas medidas podrían ser arriesgadas y causar incertidumbre económica. En lugar de eso, buscaré otras formas de estimular la economía y crear empleos, como la inversión en infraestructura y la promoción del comercio internacional. También buscaremos formas de mejorar la economía sin poner en riesgo la estabilidad financiera de nuestro país."
    }
},

    2: {
        "texto": "¿Qué medidas tomaría cada candidato para abordar la crisis ambiental y el cambio climático?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, implementaré regulaciones más estrictas para reducir las emisiones y promoveré las energías renovables.",
            "boton2": "Mi enfoque se basa en la libertad individual y la propiedad privada. No creo que exista una 'crisis' ambiental causada por el cambio climático antropogénico. En lugar de imponer regulaciones y restricciones gubernamentales, confío en la innovación tecnológica y en la capacidad de las personas para tomar decisiones informadas. Promoveré políticas que fomenten la propiedad privada y los derechos de propiedad, lo que incentivará a las personas a cuidar del medio ambiente de manera responsable.",
            "boton1": "Aunque tengo dudas sobre la magnitud del cambio climático causado por la actividad humana, reconozco la importancia de la protección del medio ambiente. Abogaré por un enfoque equilibrado que promueva la innovación y la inversión en tecnologías limpias sin imponer regulaciones excesivas. Es esencial mantener un equilibrio entre la conservación ambiental y el desarrollo económico.",
            "boton0": "No considero que el cambio climático sea un problema real ni que requiera medidas especiales. No tomaré ninguna acción para abordar lo que veo como una preocupación exagerada. Mi enfoque se centrará en otros asuntos y en la reducción de la intervención gubernamental en la economía."
        },
        "respuestas_Bullrich": {
            "refute": "Yo, Bullrich, promoveré la inversión en tecnologías limpias y la cooperación internacional para abordar el cambio climático.",
            "boton2": "Mi enfoque se basa en la libertad individual y la propiedad privada. No creo que exista una 'crisis' ambiental causada por el cambio climático antropogénico. En lugar de imponer regulaciones y restricciones gubernamentales, confío en la innovación tecnológica y en la capacidad de las personas para tomar decisiones informadas. Promoveré políticas que fomenten la propiedad privada y los derechos de propiedad, lo que incentivará a las personas a cuidar del medio ambiente de manera responsable.",
            "boton1": "Aunque tengo dudas sobre la magnitud del cambio climático causado por la actividad humana, reconozco la importancia de la protección del medio ambiente. Abogaré por un enfoque equilibrado que promueva la innovación y la inversión en tecnologías limpias sin imponer regulaciones excesivas. Es esencial mantener un equilibrio entre la conservación ambiental y el desarrollo económico.",
            "boton0": "No considero que el cambio climático sea un problema real ni que requiera medidas especiales. No tomaré ninguna acción para abordar lo que veo como una preocupación exagerada. Mi enfoque se centrará en otros asuntos y en la reducción de la intervención gubernamental en la economía."
        }
    },
    3: {
    "texto": "¿Cómo planea cada candidato reducir la inseguridad y el crimen en el país?",
    "respuestas_Massa": {
        "refute": "Yo, Massa, propongo un enfoque integral que incluye la inversión en programas sociales y el fortalecimiento de las fuerzas de seguridad.",
        "boton2": "Mi enfoque principal para reducir la inseguridad y el crimen en nuestro país es llevar a cabo una reforma completa de todas las leyes de seguridad. Esto incluye revisar y modernizar nuestro sistema judicial y legal, asegurando que las penas sean proporcionales y efectivas. Además, promoveré la cooperación entre las fuerzas de seguridad y la comunidad, fomentando una mayor participación ciudadana en la seguridad pública. La reforma de las leyes de seguridad es esencial para restaurar el orden y la paz en nuestra sociedad.",
        "boton1": "Si bien es importante abordar la inseguridad y el crimen, creo que debemos ser cautelosos al llevar a cabo una reforma total de las leyes de seguridad. Estoy dispuesto a considerar cambios y mejoras en el sistema legal y judicial, pero debemos garantizar que cualquier reforma no tenga efectos secundarios negativos. Trabajaré con expertos en seguridad y legisladores para encontrar un equilibrio entre la reforma necesaria y la protección de los derechos de los ciudadanos.",
        "boton0": "Propongo fortalecer la presencia militar en nuestras calles y comunidades como una medida inmediata para abordar la inseguridad. Esto enviará un mensaje claro de que estamos comprometidos a restaurar la ley y el orden de manera efectiva. Además, aumentaré las penas para los delincuentes y promoveré una política de 'cero tolerancia'. Necesitamos medidas firmes y directas para combatir el crimen en todas sus formas."
   },
    "respuestas_Bullrich": {
        "refute": "Yo, Bullrich, abogo por una mayor presencia policial y la implementación de políticas de seguridad basadas en la libertad individual.",
        "boton2": "Mi enfoque principal para reducir la inseguridad y el crimen en nuestro país es llevar a cabo una reforma completa de todas las leyes de seguridad. Esto incluye revisar y modernizar nuestro sistema judicial y legal, asegurando que las penas sean proporcionales y efectivas. Además, promoveré la cooperación entre las fuerzas de seguridad y la comunidad, fomentando una mayor participación ciudadana en la seguridad pública. La reforma de las leyes de seguridad es esencial para restaurar el orden y la paz en nuestra sociedad.",
        "boton1": "Si bien es importante abordar la inseguridad y el crimen, creo que debemos ser cautelosos al llevar a cabo una reforma total de las leyes de seguridad. Estoy dispuesto a considerar cambios y mejoras en el sistema legal y judicial, pero debemos garantizar que cualquier reforma no tenga efectos secundarios negativos. Trabajaré con expertos en seguridad y legisladores para encontrar un equilibrio entre la reforma necesaria y la protección de los derechos de los ciudadanos.",
        "boton0": "Propongo fortalecer la presencia militar en nuestras calles y comunidades como una medida inmediata para abordar la inseguridad. Esto enviará un mensaje claro de que estamos comprometidos a restaurar la ley y el orden de manera efectiva. Además, aumentaré las penas para los delincuentes y promoveré una política de 'cero tolerancia'. Necesitamos medidas firmes y directas para combatir el crimen en todas sus formas."
    }
},

    4: {
        "texto": "¿Cuál es la posición de cada candidato sobre la atención médica y el sistema de salud?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, abogo por un sistema de salud universal financiado principalmente a través de impuestos, con el objetivo de garantizar el acceso igualitario a la atención médica para todos los ciudadanos. Creo en un enfoque enérgico del Estado en el sector de la salud para brindar servicios médicos de calidad y asequibles a toda la población.",
            "boton2": "Promuevo un enfoque radicalmente diferente en el sistema de salud. Abogaré por la implementación de un sistema de salud basado en el mercado, donde la competencia entre proveedores de atención médica sea la norma. Esto significa fomentar la participación del sector privado, otorgar a las personas la libertad de elegir sus seguros médicos y proveedores de atención, y reducir la intervención del Estado en la salud. Creo en la capacidad de los individuos para tomar decisiones informadas sobre su atención médica y buscar opciones que se adapten a sus necesidades y presupuestos.",
            "boton1": "Si bien reconozco que hay áreas de mejora en el sistema de salud actual, mi enfoque no es tan radical como el de algunos otros candidatos. Trabajaré para mejorar la calidad y accesibilidad de la atención médica pública y reducir la burocracia en el sistema de salud. Creo que una combinación de sector público y privado puede ser efectiva para garantizar que todos tengan acceso a atención médica de calidad.",
            "boton0": "Propongo una transformación completa en nuestro sistema de salud. Abogaré por la privatización de los servicios de salud y la eliminación de la intervención estatal en la atención médica. Esto permitirá que el mercado regule la calidad y los costos de la atención médica, lo que beneficiará a los ciudadanos al brindarles opciones más amplias y competitivas. También impulsaré la implementación de un sistema de financiamiento basado en seguros privados para empoderar a las personas en la toma de decisiones sobre su atención médica."
        },
        "respuestas_Bullrich": {
            "refute": "Yo, Bullrich, promuevo un sistema de atención médica más estatal financiado por impuestos para garantizar el acceso a todos los ciudadanos. Creo en la importancia de la inversión pública en la salud para asegurarnos de que nadie se quede sin atención médica de calidad.",
            "boton2": "Promuevo un enfoque radicalmente diferente en el sistema de salud. Abogaré por la implementación de un sistema de salud basado en el mercado, donde la competencia entre proveedores de atención médica sea la norma. Esto significa fomentar la participación del sector privado, otorgar a las personas la libertad de elegir sus seguros médicos y proveedores de atención, y reducir la intervención del Estado en la salud. Creo en la capacidad de los individuos para tomar decisiones informadas sobre su atención médica y buscar opciones que se adapten a sus necesidades y presupuestos.",
            "boton1": "Si bien reconozco que hay áreas de mejora en el sistema de salud actual, mi enfoque no es tan radical como el de algunos otros candidatos. Trabajaré para mejorar la calidad y accesibilidad de la atención médica pública y reducir la burocracia en el sistema de salud. Creo que una combinación de sector público y privado puede ser efectiva para garantizar que todos tengan acceso a atención médica de calidad.",
            "boton0": "Propongo una transformación completa en nuestro sistema de salud. Abogaré por la privatización de los servicios de salud y la eliminación de la intervención estatal en la atención médica. Esto permitirá que el mercado regule la calidad y los costos de la atención médica, lo que beneficiará a los ciudadanos al brindarles opciones más amplias y competitivas. También impulsaré la implementación de un sistema de financiamiento basado en seguros privados para empoderar a las personas en la toma de decisiones sobre su atención médica."
    }
    },
    5: {
        "texto": "¿Cómo abordarían los candidatos la desigualdad de ingresos en la sociedad?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, propongo un aumento de impuestos a los más ricos y la implementación de programas de redistribución de la riqueza.",
            "boton2": "Para abordar la desigualdad de ingresos en la sociedad, propongo un enfoque basado en la libertad económica y la reducción de la intervención estatal en la economía. Creo firmemente que la prosperidad se logra a través del libre mercado y la competencia. Promoveré políticas que eliminen regulaciones innecesarias, reduzcan los impuestos y fomenten la inversión y la creación de empleos. Esto permitirá que las personas tengan más oportunidades para mejorar sus ingresos y prosperar económicamente.",
            "boton1": "Reconozco que la desigualdad de ingresos es un problema, y estoy dispuesto a tomar medidas para abordarlo de manera equitativa. Mi enfoque será implementar políticas de redistribución de ingresos y aumentar la carga fiscal sobre los más ricos para financiar programas sociales que beneficien a los menos privilegiados. Además, trabajaré en la creación de empleos y oportunidades económicas para reducir la brecha de ingresos.",
            "boton0": "Creo que el gobierno debe desempeñar un papel activo en la igualación de los ingresos en la sociedad. Abogaré por un mayor control estatal en la economía, incluida la implementación de impuestos progresivos y regulaciones más estrictas sobre las empresas. También promoveré la expansión de programas sociales financiados por el Estado para garantizar que nadie quede rezagado en términos de ingresos. La igualdad económica será una de mis principales prioridades."
        },
        "respuestas_Bullrich": {
            "refute": "Mi enfoque para abordar la desigualdad de ingresos se centra en políticas que fomenten la inversión y el crecimiento económico. Busco reducir la carga impositiva sobre la clase trabajadora y las pequeñas empresas, al tiempo que promuevo la creación de empleo y oportunidades para todos los ciudadanos. Creo que al fortalecer la economía, podemos reducir las disparidades de ingresos y mejorar la calidad de vida de las personas.",
            "boton2": "Para abordar la desigualdad de ingresos en la sociedad, propongo un enfoque basado en la libertad económica y la reducción de la intervención estatal en la economía. Creo firmemente que la prosperidad se logra a través del libre mercado y la competencia. Promoveré políticas que eliminen regulaciones innecesarias, reduzcan los impuestos y fomenten la inversión y la creación de empleos. Esto permitirá que las personas tengan más oportunidades para mejorar sus ingresos y prosperar económicamente.",
            "boton1": "Reconozco que la desigualdad de ingresos es un problema, y estoy dispuesto a tomar medidas para abordarlo de manera equitativa. Mi enfoque será implementar políticas de redistribución de ingresos y aumentar la carga fiscal sobre los más ricos para financiar programas sociales que beneficien a los menos privilegiados. Además, trabajaré en la creación de empleos y oportunidades económicas para reducir la brecha de ingresos.",
            "boton0": "Creo que el gobierno debe desempeñar un papel activo en la igualación de los ingresos en la sociedad. Abogaré por un mayor control estatal en la economía, incluida la implementación de impuestos progresivos y regulaciones más estrictas sobre las empresas. También promoveré la expansión de programas sociales financiados por el Estado para garantizar que nadie quede rezagado en términos de ingresos. La igualdad económica será una de mis principales prioridades."

        }
    },
    6: {
        "texto": "¿Qué políticas proponen los candidatos para mejorar la infraestructura y el transporte público?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, propongo una mayor inversión estatal en infraestructura y transporte público para mejorar la accesibilidad.",
               "boton2": "Impulsaré un régimen de iniciativa privada similar al modelo chileno para financiar obras de infraestructura, fomentando la inversión empresarial y la participación de los usuarios. Este enfoque busca eliminar la corrupción y garantizar la eficiencia en las obras públicas.",
               "boton1": "Considero que es necesario reformar el sistema actual de obra pública para reducir la corrupción y aumentar la eficiencia.",
               "boton0": "Mantendré el sistema de obra pública actual financiado por impuestos, ya que creo que es la mejor manera de asegurar la inversión en infraestructura y transporte público."
},
        "respuestas_Bullrich": {
            "refute": "Yo, Bullrich, abogo por la inversión en obra publica e intervención estatal en el transporte público.",
            "boton2": "Promoveré un sistema de inversión privada en proyectos de infraestructura, siguiendo el modelo chileno. Esto eliminará la corrupción y garantizará la eficiencia en las obras públicas, permitiendo a los empresarios asumir el riesgo y a los usuarios pagar por las obras.",
            "boton1": "Considero importante reformar el sistema actual de inversión en infraestructura para reducir la corrupción y mejorar la eficiencia. Favorecería una mayor inversión privada y menos intervención estatal.",
            "boton0": "Mantendré el sistema actual de inversión pública financiado por impuestos, ya que creo que es la mejor manera de asegurar la inversión en infraestructura y transporte público."
}
    },
    7: {
        "texto": "¿Cuál es la postura de cada candidato sobre la inmigración y las políticas de fronteras?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, abogo por un enfoque más restrictivo en la inmigración y un mayor control en las fronteras para proteger a los ciudadanos locales.",
            "boton2": "Mi enfoque en inmigración y políticas de fronteras se basa en la idea de la libertad individual y la responsabilidad. Defiendo un sistema que permita la inmigración abierta, pero también creo que aquellos que elijan vivir en nuestro país deben contribuir a su sostenibilidad. Por lo tanto, propongo que los extranjeros paguen por los servicios públicos que utilicen, de manera justa y equitativa. Esto garantizará una inmigración ordenada y beneficiosa para todos.",
            "boton1": "Entiendo la importancia de la inmigración para enriquecer nuestra sociedad y economía, pero también creo que debemos ser responsables en su gestión. Apoyaré políticas que fomenten una inmigración controlada y legal, con ciertas regulaciones para garantizar la seguridad y el bienestar de todos los residentes. Consideraré medidas para equilibrar los beneficios de la inmigración con las responsabilidades que conlleva.",
            "boton0": "Mi posición sobre inmigración es clara: abogaré por una política de puertas abiertas y eliminaré cualquier restricción en las fronteras. No creo en imponer cargas adicionales a los extranjeros que elijan vivir en nuestro país. La libertad de movimiento y la inclusión son fundamentales en mi visión, y no apoyaré ninguna medida que restrinja la inmigración o exija pagos adicionales a los inmigrantes."
        },
        "respuestas_Bullrich": {
            "refute": "Yo, Bullrich, abogo por un enfoque más restrictivo en la inmigración y un mayor control en las fronteras para proteger a los ciudadanos locales.",
            "boton2": "Mi enfoque en inmigración y políticas de fronteras se basa en la idea de la libertad individual y la responsabilidad. Defiendo un sistema que permita la inmigración abierta, pero también creo que aquellos que elijan vivir en nuestro país deben contribuir a su sostenibilidad. Por lo tanto, propongo que los extranjeros paguen por los servicios públicos que utilicen, de manera justa y equitativa. Esto garantizará una inmigración ordenada y beneficiosa para todos.",
            "boton1": "Entiendo la importancia de la inmigración para enriquecer nuestra sociedad y economía, pero también creo que debemos ser responsables en su gestión. Apoyaré políticas que fomenten una inmigración controlada y legal, con ciertas regulaciones para garantizar la seguridad y el bienestar de todos los residentes. Consideraré medidas para equilibrar los beneficios de la inmigración con las responsabilidades que conlleva.",
            "boton0": "Mi posición sobre inmigración es clara: abogaré por una política de puertas abiertas y eliminaré cualquier restricción en las fronteras. No creo en imponer cargas adicionales a los extranjeros que elijan vivir en nuestro país. La libertad de movimiento y la inclusión son fundamentales en mi visión, y no apoyaré ninguna medida que restrinja la inmigración o exija pagos adicionales a los inmigrantes."
        }
    },
    8: {
        "texto": "¿Cómo planean los candidatos fomentar la inversión extranjera y el comercio internacional?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, abogo por una mayor regulación en la inversión extranjera y restricciones para proteger nuestros intereses nacionales.",
            "boton2": "Mi enfoque para fomentar la inversión extranjera y el comercio internacional se basa en principios de apertura económica y competitividad. Propongo la dolarización de nuestra economía para brindar estabilidad y confianza a los inversores extranjeros. Además, reduciré significativamente los impuestos y regulaciones que actualmente pueden obstaculizar la inversión y el comercio. Esto hará que Argentina sea un lugar atractivo para los negocios internacionales y ayudará a crear empleos y crecimiento económico.",
            "boton1": "Si bien reconozco la importancia de atraer inversión extranjera y fomentar el comercio internacional, también creo que debemos ser cautelosos y proteger los intereses nacionales. Mantendré un equilibrio entre la apertura económica y la protección de nuestra industria local. Evaluaré cuidadosamente cualquier medida que pueda afectar a la economía nacional y tomaré decisiones basadas en el interés argentino.",
            "boton0": "No apoyo la apertura económica ni la inversión extranjera. Creo que debemos proteger nuestra industria local y mantener un control estricto sobre nuestro comercio internacional. No permitiré la dolarización de la economía ni la reducción de impuestos para atraer inversores extranjeros. Debemos preservar nuestros recursos y empleos para los argentinos y evitar cualquier influencia extranjera en nuestra economía."
        },
        "respuestas_Bullrich": {
            "refute": "Yo, Bullrich, abogo por la eliminación de barreras al comercio internacional para atraer inversión extranjera.",
            "boton2": "Mi enfoque para fomentar la inversión extranjera y el comercio internacional se basa en principios de apertura económica y competitividad. Propongo la dolarización de nuestra economía para brindar estabilidad y confianza a los inversores extranjeros. Además, reduciré significativamente los impuestos y regulaciones que actualmente pueden obstaculizar la inversión y el comercio. Esto hará que Argentina sea un lugar atractivo para los negocios internacionales y ayudará a crear empleos y crecimiento económico.",
            "boton1": "Si bien reconozco la importancia de atraer inversión extranjera y fomentar el comercio internacional, también creo que debemos ser cautelosos y proteger los intereses nacionales. Mantendré un equilibrio entre la apertura económica y la protección de nuestra industria local. Evaluaré cuidadosamente cualquier medida que pueda afectar a la economía nacional y tomaré decisiones basadas en el interés argentino.",
            "boton0": "No apoyo la apertura económica ni la inversión extranjera. Creo que debemos proteger nuestra industria local y mantener un control estricto sobre nuestro comercio internacional. No permitiré la dolarización de la economía ni la reducción de impuestos para atraer inversores extranjeros. Debemos preservar nuestros recursos y empleos para los argentinos y evitar cualquier influencia extranjera en nuestra economía."
        }
    },
    9: {
        "texto": "¿Cuáles son las estrategias de cada candidato para garantizar la transparencia y la lucha contra la corrupción en el gobierno?",
        "respuestas_Massa": {
            "refute": "Yo, Massa, propongo fortalecer las instituciones gubernamentales y aumentar la regulación para prevenir la corrupción.",
            "boton2": "Mi enfoque para garantizar la transparencia y luchar contra la corrupción se basa en principios de mercado libre y limitación del poder estatal. Propongo reducir el tamaño y alcance del gobierno, eliminando regulaciones innecesarias y burocracia. Esto minimiza las oportunidades para la corrupción. Además, defenderé la independencia del poder judicial y la protección de los derechos individuales, lo que contribuye a un gobierno más transparente y menos corrupto.",
            "boton1": "Reconozco la importancia de garantizar la transparencia y combatir la corrupción en el gobierno. Si bien comparto la necesidad de reducir la burocracia y mejorar la eficiencia del Estado, también creo que debemos mantener ciertas regulaciones y controles para prevenir la corrupción. Buscaré un equilibrio entre la reducción del poder estatal y la necesidad de supervisión para prevenir malas prácticas.",
            "boton0": "No creo que la transparencia y la lucha contra la corrupción sean prioridades. Mi enfoque se centra en expandir el poder del Estado y en la intervención estatal en la economía. Esto puede aumentar el riesgo de corrupción, pero considero que es un costo necesario para lograr mis objetivos de gobierno. La Escuela Austriaca de Economía no es mi principal influencia en este tema."
        },
        "respuestas_Bullrich": {
            "refute": "Yo, Bullrich, propongo fortalecer las instituciones gubernamentales y aumentar la regulación para prevenir la corrupción.",
            "boton2": "Mi enfoque para garantizar la transparencia y luchar contra la corrupción se basa en principios de mercado libre y limitación del poder estatal. Propongo reducir el tamaño y alcance del gobierno, eliminando regulaciones innecesarias y burocracia. Esto minimiza las oportunidades para la corrupción. Además, defenderé la independencia del poder judicial y la protección de los derechos individuales, lo que contribuye a un gobierno más transparente y menos corrupto.",
            "boton1": "Reconozco la importancia de garantizar la transparencia y combatir la corrupción en el gobierno. Si bien comparto la necesidad de reducir la burocracia y mejorar la eficiencia del Estado, también creo que debemos mantener ciertas regulaciones y controles para prevenir la corrupción. Buscaré un equilibrio entre la reducción del poder estatal y la necesidad de supervisión para prevenir malas prácticas.",
            "boton0": "No creo que la transparencia y la lucha contra la corrupción sean prioridades. Mi enfoque se centra en expandir el poder del Estado y en la intervención estatal en la economía. Esto puede aumentar el riesgo de corrupción, pero considero que es un costo necesario para lograr mis objetivos de gobierno. La Escuela Austriaca de Economía no es mi principal influencia en este tema."
        }
    },
    # Agrega más preguntas aquí
}

preguntas_B = {
    0: {
        "texto": "¿Cómo abordaría cada candidato el problema de la educación en el país?",
        "respuestas_Milei": {
            "refute": "Abogo por la libertad de elección en la educación y menos intervención estatal. Esto permite a los padres decidir la mejor educación para sus hijos.",
            "boton2": "Creo en una educación de calidad a través de la inversión estatal y la regulación adecuada.",
            "boton1": "Defiendo un control total del Estado en la educación.",
            "boton0": "Buscaré un equilibrio entre la libertad de elección y la regulación en la educación."
        },
        "respuestas_Bullrich": {
            "refute": "Daré más autonomía a las provincias en este tema.",
            "boton2": "Creo en una educación de calidad a través de la inversión estatal y la regulación adecuada.",
            "boton1": "Defiendo un control total del Estado en la educación.",
            "boton0": "Buscaré un equilibrio entre la libertad de elección y la regulación en la educación."
        }
    },
    1: {
        "texto": "¿Cuál es la propuesta de cada candidato para mejorar la economía y crear empleos?",
        "respuestas_Milei": {
            "refute": "Defiendo un enfoque de mercado libre para fomentar la inversión y el crecimiento económico. Menos regulaciones y menos impuestos estimulan la creación de empleo.",
            "boton2": "Creo en una mayor regulación estatal y la redistribución de la riqueza para estimular la economía.",
            "boton1": "Buscaré un equilibrio entre el mercado libre y la regulación estatal para promover el empleo.",
            "boton0": "Aumentaré las regulaciones y los impuestos para redistribuir la riqueza."
        },
        "respuestas_Bullrich": {
            "refute": "Defiendo un enfoque de mercado libre y la inversión privada para estimular la economía y crear empleos.",
            "boton2": "Creo en una mayor regulación estatal y la redistribución de la riqueza para estimular la economía.",
            "boton1": "Buscaré un equilibrio entre el mercado libre y la regulación estatal para promover el empleo.",
            "boton0": "Aumentaré las regulaciones y los impuestos para redistribuir la riqueza."
        }
    },
    2: {
        "texto": "¿Qué medidas tomaría cada candidato para abordar la crisis ambiental y el cambio climático?",
        "respuestas_Milei": {
            "refute": "¿?",
            "boton2": "Creo en una mayor regulación ambiental y la transición hacia energías limpias.",
            "boton1": "Buscaré un equilibrio entre la protección del medio ambiente y el crecimiento económico.",
            "boton0": "No considero urgente abordar el cambio climático."
        },
        "respuestas_Bullrich": {
            "refute": "Promoveré la inversión en tecnologías limpias y la cooperación internacional para abordar el cambio climático.",
            "boton2": "Creo en una mayor regulación ambiental y la transición hacia energías limpias.",
            "boton1": "Buscaré un equilibrio entre la protección del medio ambiente y el crecimiento económico.",
            "boton0": "No considero urgente abordar el cambio climático."
        }
    },
    3: {
        "texto": "¿Cómo planea cada candidato reducir la inseguridad y el crimen en el país?",
        "respuestas_Milei": {
            "refute": "Implementación de políticas basadas en la libertad individual para combatir el crimen.",
            "boton2": "Creo en una estrategia integral que incluye inversión en programas sociales y el fortalecimiento de las fuerzas de seguridad.",
            "boton1": "Buscaré un equilibrio entre medidas de seguridad y programas sociales para reducir el crimen.",
            "boton0": "Aumentaré las penas de prisión y aplicaré un enfoque de mano dura contra el crimen."
        },
        "respuestas_Bullrich": {
            "refute": "Abogo por una mayor presencia policial.",
            "boton2": "Creo en una estrategia integral que incluye inversión en programas sociales y el fortalecimiento de las fuerzas de seguridad.",
            "boton1": "Buscaré un equilibrio entre medidas de seguridad y programas sociales para reducir el crimen.",
            "boton0": "Aumentaré las penas de prisión y aplicaré un enfoque de mano dura contra el crimen."
        }
    },
    4: {
        "texto": "¿Cuál es la posición de cada candidato sobre la atención médica y el sistema de salud?",
        "respuestas_Milei": {
            "refute": "Abogo por la competencia en el sector de la salud y menos regulaciones para mejorar la calidad y accesibilidad.",
            "boton2": "Creo en un sistema de salud universal financiado por impuestos para garantizar el acceso a todos los ciudadanos.",
            "boton1": "Buscaré un equilibrio entre la competencia y la regulación en el sector de la salud.",
            "boton0": "Fortaleceré el sistema de salud privado y reduciré la intervención estatal."
        },
        "respuestas_Bullrich": {
            "refute": "Abogo por la competencia en el sector de la salud y menos regulaciones para mejorar la calidad y accesibilidad.",
            "boton2": "Creo en un sistema de salud universal financiado por impuestos para garantizar el acceso a todos los ciudadanos.",
            "boton1": "Buscaré un equilibrio entre la competencia y la regulación en el sector de la salud.",
            "boton0": "Fortaleceré el sistema de salud privado y reduciré la intervención estatal."
        }
    },
    5: {
        "texto": "¿Cómo abordarían los candidatos la desigualdad de ingresos en la sociedad?",
        "respuestas_Milei": {
            "refute": "Abogo por reducir los impuestos y promover la libertad económica para estimular la prosperidad y reducir la desigualdad.",
            "boton2": "Aumentaré los impuestos a los más ricos y redistribuiré la riqueza para reducir la desigualdad.",
            "boton1": "Buscaré un equilibrio entre la reducción de impuestos y la redistribución de la riqueza.",
            "boton0": "Reduciré la libertad económica y aumentaré los impuestos para igualar los ingresos."
        },
        "respuestas_Bullrich": {
            "refute": "Abogo por reducir los impuestos y promover la libertad económica para estimular la prosperidad y reducir la desigualdad.",
            "boton2": "Aumentaré los impuestos a los más ricos y redistribuiré la riqueza para reducir la desigualdad.",
            "boton1": "Buscaré un equilibrio entre la reducción de impuestos y la redistribución de la riqueza.",
            "boton0": "Reduciré la libertad económica y aumentaré los impuestos para igualar los ingresos."
        }
    },
    6: {
        "texto": "¿Qué políticas proponen los candidatos para mejorar la infraestructura y el transporte público?",
        "respuestas_Milei": {
            "refute": "Abogo por la inversión privada en infraestructura y menos intervención estatal en el transporte público para mejorar la eficiencia y la calidad.",
            "boton2": "Creo en una mayor inversión estatal en infraestructura y transporte público para mejorar la accesibilidad.",
            "boton1": "Buscaré un equilibrio entre la inversión privada y la inversión estatal en infraestructura.",
            "boton0": "Estableceré un control estatal total en infraestructura y transporte."
        },
        "respuestas_Bullrich": {
            "refute": "Abogo por la inversión privada en infraestructura y menos intervención estatal en el transporte público para mejorar la eficiencia y la calidad.",
            "boton2": "Creo en una mayor inversión estatal en infraestructura y transporte público para mejorar la accesibilidad.",
            "boton1": "Buscaré un equilibrio entre la inversión privada y la inversión estatal en infraestructura.",
            "boton0": "Estableceré un control estatal total en infraestructura y transporte."
        }
    },
    7: {
        "texto": "¿Cuál es la postura de cada candidato sobre la inmigración y las políticas de fronteras?",
        "respuestas_Milei": {
            "refute": "Defiendo una política de puertas abiertas y eliminaré las restricciones en las fronteras para promover la libertad de movimiento.",
            "boton2": "Abogaré por un enfoque más restrictivo en la inmigración y un mayor control en las fronteras para proteger a los ciudadanos locales.",
            "boton1": "Buscaré un equilibrio entre una política de inmigración abierta y el control de fronteras.",
            "boton0": "Defenderé restricciones severas en la inmigración y en las políticas de fronteras."
        },
        "respuestas_Bullrich": {
            "refute": "Defiendo un enfoque más restrictivo en la inmigración y un mayor control en las fronteras para proteger a los ciudadanos locales.",
            "boton2": "Abogaré por un enfoque más restrictivo en la inmigración y un mayor control en las fronteras para proteger a los ciudadanos locales.",
            "boton1": "Buscaré un equilibrio entre una política de inmigración abierta y el control de fronteras.",
            "boton0": "Defenderé restricciones severas en la inmigración y en las políticas de fronteras."
        }
    },
    8: {
        "texto": "¿Cómo planean los candidatos fomentar la inversión extranjera y el comercio internacional?",
        "respuestas_Milei": {
            "refute": "Abogo por la apertura económica y la eliminación de barreras al comercio internacional para atraer inversión extranjera y estimular la economía.",
            "boton2": "Creo en una mayor regulación en la inversión extranjera y restricciones para proteger nuestros intereses nacionales.",
            "boton1": "Buscaré un equilibrio entre la inversión extranjera y la protección de nuestros recursos.",
            "boton0": "Impondré restricciones severas a la inversión extranjera y limitaré el comercio internacional."
        },
        "respuestas_Bullrich": {
            "refute": "Abogo por la apertura económica y la eliminación de barreras al comercio internacional para atraer inversión extranjera y estimular la economía.",
            "boton2": "Creo en una mayor regulación en la inversión extranjera y restricciones para proteger nuestros intereses nacionales.",
            "boton1": "Buscaré un equilibrio entre la inversión extranjera y la protección de nuestros recursos.",
            "boton0": "Impondré restricciones severas a la inversión extranjera y limitaré el comercio internacional."
        }
    },
    9: {
        "texto": "¿Cuáles son las estrategias de cada candidato para garantizar la transparencia y la lucha contra la corrupción en el gobierno?",
        "respuestas_Milei": {
            "refute": "Abogaré por una menor intervención del Estado y la reducción de regulaciones como medio para combatir la corrupción.",
            "boton2": "Fortaleceré las instituciones gubernamentales y aumentaré la regulación para prevenir la corrupción.",
            "boton1": "Buscaré un equilibrio entre regulación y transparencia gubernamental.",
            "boton0": "Reduzco la burocracia y la regulación gubernamental para prevenir la corrupción."
        },
        "respuestas_Bullrich": {
            "refute": "Propondré fortalecer las instituciones gubernamentales y aumentar la regulación para prevenir la corrupción y aumentar la eficiencia del gobierno.",
            "boton2": "Fortaleceré las instituciones gubernamentales y aumentaré la regulación para prevenir la corrupción.",
            "boton1": "Buscaré un equilibrio entre regulación y transparencia gubernamental.",
            "boton0": "Reduzco la burocracia y la regulación gubernamental para prevenir la corrupción."
        }
    },
    # Agrega más preguntas aquí
}

preguntas_C = {
    0: {
        "texto": "¿Cómo abordaría cada candidato el problema de la educación en el país?",
        "respuestas_Milei": {
            "refute": "En mi visión, creo que la educación debe ser descentralizada y liberada de regulaciones excesivas a nivel nacional. Propongo implementar un sistema de vouchers que permita a los padres elegir libremente la educación que mejor se adapte a las necesidades de sus hijos. Esto fomentará la competencia entre las instituciones educativas y llevará a una mejora en la calidad de la educación en todo el país.",
            "boton2": "Buscaré un equilibrio entre regulaciones y mercado en la educación, promoviendo la colaboración entre el Estado y las instituciones educativas para garantizar una educación de calidad.",
            "boton1": "Creo que la educación debe ser regulada a nivel nacional para garantizar la calidad y la equidad en todo el país, mientras aún se promueve la innovación y la diversidad en la enseñanza.",
            "boton0": "No defiendo un control total del Estado en la educación, pero considero que el Estado debe tener un papel activo en la supervisión y regulación de las instituciones educativas para asegurar que cumplan con los estándares de calidad y equidad."
        },
        "respuestas_Massa": {
            "refute": "En mi visión, propongo una mayor inversión estatal para garantizar una educación de calidad para todos los argentinos.",
            "boton2": "Buscaré un equilibrio entre regulaciones y mercado en la educación, promoviendo la colaboración entre el Estado y las instituciones educativas para garantizar una educación de calidad.",
            "boton1": "Creo que la educación debe ser regulada a nivel nacional para garantizar la calidad y la equidad en todo el país, mientras aún se promueve la innovación y la diversidad en la enseñanza.",
            "boton0": "No defiendo un control total del Estado en la educación, pero considero que el Estado debe tener un papel activo en la supervisión y regulación de las instituciones educativas para asegurar que cumplan con los estándares de calidad y equidad."
        }
    },
    1: {
        "texto": "¿Cuál es la propuesta de cada candidato para mejorar la economía y crear empleos?",
        "respuestas_Milei": {
            "refute": "Mi propuesta para mejorar la economía y crear empleos se basa en la reducción drástica de la intervención estatal en la economía. Promoveré la eliminación de regulaciones innecesarias y burocracia que obstaculizan a las empresas. También buscaré reducir la carga impositiva y simplificar el sistema tributario para fomentar la inversión y el emprendimiento. Además, promoveré la apertura comercial y la competencia para que las empresas puedan crecer y generar empleos de manera más eficiente. Creo que el libre mercado es el motor que impulsará el crecimiento económico y la creación de empleos en nuestro país.",
            "boton2": "Mi propuesta para mejorar la economía y crear empleos se basa en una combinación equilibrada de políticas públicas y mercado. Buscaré incentivar la inversión en sectores estratégicos, al tiempo que mantendré regulaciones adecuadas para garantizar condiciones laborales justas y proteger a los trabajadores. También promoveré la inversión en educación y capacitación para mejorar la fuerza laboral y fomentar la innovación.",
            "boton1": "Creo que es importante equilibrar la intervención estatal y el mercado para mejorar la economía y crear empleos. Mantendré regulaciones que sean necesarias para proteger a los trabajadores y garantizar la competencia justa, pero también buscaré incentivar la inversión y el emprendimiento. La educación y la capacitación serán una prioridad para mejorar la cualificación de nuestra fuerza laboral.",
            "boton0": "Aumentaré la regulación y los impuestos para redistribuir la riqueza."
        },
        "respuestas_Massa": {
            "refute": "Mi propuesta para mejorar la economía y crear empleos se basa en políticas públicas sólidas y una regulación adecuada. Buscaré implementar políticas que promuevan la inversión en sectores estratégicos y protejan a los trabajadores. También enfocaré mis esfuerzos en fortalecer la seguridad social y el bienestar de la población, garantizando la equidad en la distribución de la riqueza.",
            "boton2": "Mi propuesta para mejorar la economía y crear empleos se basa en una combinación equilibrada de políticas públicas y mercado. Buscaré incentivar la inversión en sectores estratégicos, al tiempo que mantendré regulaciones adecuadas para garantizar condiciones laborales justas y proteger a los trabajadores. También promoveré la inversión en educación y capacitación para mejorar la fuerza laboral y fomentar la innovación.",
            "boton1": "Creo que es importante equilibrar la intervención estatal y el mercado para mejorar la economía y crear empleos. Mantendré regulaciones que sean necesarias para proteger a los trabajadores y garantizar la competencia justa, pero también buscaré incentivar la inversión y el emprendimiento. La educación y la capacitación serán una prioridad para mejorar la cualificación de nuestra fuerza laboral.",
            "boton0": "Defiendo una intervención estatal total en la economía para mejorar la economía y crear empleos. Implementaré regulaciones estrictas y controlaré directamente la producción y la distribución de bienes y servicios. Además, aumentaré los impuestos a las grandes empresas y redistribuiré los ingresos de manera más equitativa para reducir las desigualdades económicas."
        }
    },
    2: {
        "texto": "¿Qué medidas tomaría cada candidato para abordar la crisis ambiental y el cambio climático?",
        "respuestas_Milei": {
            "refute": "Considero que las preocupaciones sobre el cambio climático están basadas en datos poco confiables y que las políticas ambientales excesivas son perjudiciales para la economía. Mi enfoque será eliminar regulaciones innecesarias y promover la libertad económica. No creo que sea necesario tomar medidas drásticas para abordar lo que considero una exageración.",
            "boton2": "Considero que la crisis ambiental y el cambio climático son desafíos apremiantes que requieren medidas decisivas. Implementaré políticas ambientales sólidas, promoveré la inversión en energías limpias y renovables, y me comprometeré a reducir las emisiones de gases de efecto invernadero. También colaboraré activamente con la comunidad internacional para cumplir con los acuerdos climáticos globales.",
            "boton1": "Creo que es fundamental tomar medidas serias para abordar la crisis ambiental y el cambio climático. Trabajaré en la implementación de políticas verdes, promoveré la transición hacia fuentes de energía más limpias y respaldaré la conservación de nuestros recursos naturales. Mi objetivo es encontrar un equilibrio entre el desarrollo económico y la protección del medio ambiente.",
            "boton0": "Considero que las preocupaciones sobre el cambio climático están exageradas y que las regulaciones ambientales son excesivas. Priorizaré el desarrollo económico sobre las preocupaciones ambientales y reduciré las restricciones que afectan a las empresas. No creo que sea necesario tomar medidas drásticas para abordar la crisis climática."
        },
        "respuestas_Massa": {
            "refute": "Reconozco la importancia de abordar la crisis ambiental y el cambio climático. Promoveré políticas de conservación de recursos naturales, fomentaré la inversión en energías limpias y renovables, y buscaré reducir las emisiones de gases de efecto invernadero. Mi enfoque es encontrar un equilibrio entre el desarrollo económico y la protección del medio ambiente, garantizando que las generaciones futuras también disfruten de un entorno saludable.",
            "boton2": "Considero que la crisis ambiental y el cambio climático son desafíos apremiantes que requieren medidas decisivas. Implementaré políticas ambientales sólidas, promoveré la inversión en energías limpias y renovables, y me comprometeré a reducir las emisiones de gases de efecto invernadero. También colaboraré activamente con la comunidad internacional para cumplir con los acuerdos climáticos globales.",
            "boton1": "Creo que es fundamental tomar medidas serias para abordar la crisis ambiental y el cambio climático. Trabajaré en la implementación de políticas verdes, promoveré la transición hacia fuentes de energía más limpias y respaldaré la conservación de nuestros recursos naturales. Mi objetivo es encontrar un equilibrio entre el desarrollo económico y la protección del medio ambiente.",
            "boton0": "Considero que las preocupaciones sobre el cambio climático están exageradas y que las regulaciones ambientales son excesivas. Priorizaré el desarrollo económico sobre las preocupaciones ambientales y reduciré las restricciones que afectan a las empresas. No creo que sea necesario tomar medidas drásticas para abordar la crisis climática."
        }
    },
    3: {
        "texto": "¿Cómo planea cada candidato reducir la inseguridad y el crimen en el país?",
        "respuestas_Milei": {
            "refute": "Mi propuesta para abordar la inseguridad y el crimen es llevar a cabo una reforma completa de todas las leyes relacionadas con la justicia y la seguridad. Esto incluiría una revisión exhaustiva del sistema judicial y penitenciario, así como la eliminación de regulaciones innecesarias que limitan la capacidad de las personas para defenderse. Creo en la importancia de empoderar a los ciudadanos y reducir la intervención del Estado en sus vidas para lograr una sociedad más segura y justa.",
            "boton2": "Mi enfoque para reducir la inseguridad y el crimen se basa en una estrategia integral que combina la prevención, la inversión en educación y la reforma del sistema de justicia. Además, propongo la construcción de la cárcel DRA CFK como parte de un enfoque de rehabilitación y reinserción de los delincuentes en la sociedad. Para financiar estas iniciativas, buscaremos una combinación de recursos estatales y cooperación público-privada.",
            "boton1": "Creo que es importante abordar la inseguridad y el crimen mediante la inversión en programas de prevención y la reforma del sistema de justicia. La construcción de la cárcel DRA CFK es una propuesta interesante, pero debemos analizar cuidadosamente su financiamiento y viabilidad. Buscaré recursos estatales y posibles acuerdos de colaboración para llevar a cabo estas medidas.",
            "boton0": "Considero que la cárcel DRA CFK es una idea inadecuada y que debemos enfocarnos en reformar el sistema de justicia y fortalecer la prevención del delito. No apoyaré la construcción de esta cárcel sin un plan de financiamiento sólido y viable. Mi enfoque principal será la inversión en programas sociales y educativos para abordar las causas subyacentes de la criminalidad."
        },
        "respuestas_Massa": {
            "refute": "Para abordar la inseguridad y el crimen, propongo un enfoque que combine la inversión en programas sociales y educativos con una política de mano firme. Mi visión se basa en valores tradicionales y la importancia de fortalecer la presencia del Estado en áreas críticas. Buscaré medidas para aumentar la presencia policial en las comunidades y garantizar que las leyes existentes se apliquen de manera efectiva. También trabajaremos en programas de rehabilitación para delincuentes, pero mantendremos un enfoque en la seguridad de la comunidad.",
            "boton2": "Mi enfoque para reducir la inseguridad y el crimen se basa en una estrategia integral que combina la prevención, la inversión en educación y la reforma del sistema de justicia. Además, propongo la construcción de la cárcel DRA CFK como parte de un enfoque de rehabilitación y reinserción de los delincuentes en la sociedad. Para financiar estas iniciativas, buscaremos una combinación de recursos estatales y cooperación público-privada.",
            "boton1": "Creo que es importante abordar la inseguridad y el crimen mediante la inversión en programas de prevención y la reforma del sistema de justicia. La construcción de la cárcel DRA CFK es una propuesta interesante, pero debemos analizar cuidadosamente su financiamiento y viabilidad. Buscaré recursos estatales y posibles acuerdos de colaboración para llevar a cabo estas medidas.",
            "boton0": "Considero que la cárcel DRA CFK es una idea inadecuada y que debemos enfocarnos en reformar el sistema de justicia y fortalecer la prevención del delito. No apoyaré la construcción de esta cárcel sin un plan de financiamiento sólido y viable. Mi enfoque principal será la inversión en programas sociales y educativos para abordar las causas subyacentes de la criminalidad."
        }
    },
    4: {
        "texto": "¿Cuál es la posición de cada candidato sobre la atención médica y el sistema de salud?",
        "respuestas_Milei": {
            "refute": "Mi enfoque en la economía es claro: promoveré políticas de mercado libre y reduciré la intervención estatal en la economía tanto como sea posible. Creo en la reducción de impuestos y regulaciones para fomentar la inversión y el crecimiento económico. Además, buscaré simplificar el sistema tributario para aliviar la carga de los contribuyentes y promover la competitividad. La austeridad fiscal y el respeto por la propiedad privada son fundamentales en mi visión económica.",
            "boton2": "Mi enfoque en la atención médica y el sistema de salud se basa en una digitalización integral del sistema sanitario nacional y la estricta implementación del Plan Médico Obligatorio. Creo que es esencial garantizar que todos los ciudadanos tengan acceso a la atención médica de calidad que merecen. Además, me comprometo a mejorar el funcionamiento del PAMI y permitir que los jubilados que deseen permanecer en su Obra Social puedan hacerlo sin restricciones. La salud de los argentinos es una prioridad para mí.",
            "boton1": "Tengo la firme convicción de que debemos mejorar el sistema de salud en Argentina. Mi propuesta se centra en la digitalización del sistema sanitario y la implementación efectiva del Plan Médico Obligatorio. Además, considero importante permitir que los jubilados puedan optar por quedarse en su Obra Social si así lo desean. Sin embargo, es necesario seguir discutiendo y refinando estas propuestas para garantizar que sean beneficiosas para todos los ciudadanos.",
            "boton0": "Digitalización y del Plan Médico Obligatorio, pero no estoy seguro de cómo funcionaría eso en la práctica. Además, permitir que los jubilados elijan su Obra Social suena un poco complicado, ¿no? En general, creo que necesitamos más información."
        },
        "respuestas_Massa": {
            "refute": "En mi enfoque económico, priorizo la equidad y la justicia social. Abogaré por una intervención estatal responsable para garantizar que todos los ciudadanos tengan acceso a servicios esenciales, como atención médica, educación y vivienda. Buscaré políticas que promuevan la igualdad de oportunidades y la protección de los derechos de los trabajadores. Además, impulsaré programas de bienestar social para ayudar a aquellos en situaciones más vulnerables. En resumen, mi objetivo es equilibrar el crecimiento económico con la inclusión social.",
            "boton2": "Mi enfoque en la atención médica y el sistema de salud se basa en una digitalización integral del sistema sanitario nacional y la estricta implementación del Plan Médico Obligatorio. Creo que es esencial garantizar que todos los ciudadanos tengan acceso a la atención médica de calidad que merecen. Además, me comprometo a mejorar el funcionamiento del PAMI y permitir que los jubilados que deseen permanecer en su Obra Social puedan hacerlo sin restricciones. La salud de los argentinos es una prioridad para mí.",
            "boton1": "Tengo la firme convicción de que debemos mejorar el sistema de salud en Argentina. Mi propuesta se centra en la digitalización del sistema sanitario y la implementación efectiva del Plan Médico Obligatorio. Además, considero importante permitir que los jubilados puedan optar por quedarse en su Obra Social si así lo desean. Sin embargo, es necesario seguir discutiendo y refinando estas propuestas para garantizar que sean beneficiosas para todos los ciudadanos.",
            "boton0": "Digitalización y del Plan Médico Obligatorio, pero no estoy seguro de cómo funcionaría eso en la práctica. Además, permitir que los jubilados elijan su Obra Social suena un poco complicado, ¿no? En general, creo que necesitamos más información."
        }
    },
    5: {
        "texto": "¿Cómo abordarían los candidatos la desigualdad de ingresos en la sociedad?",
        "respuestas_Milei": {
            "refute": "Mi enfoque en la desigualdad es promover la reducción de impuestos y la promoción de la libertad económica para estimular la prosperidad.",
            "boton2": "Para abordar la desigualdad de ingresos, propongo implementar políticas sociales y económicas equitativas. Esto incluye la redistribución de la riqueza a través de impuestos progresivos para aquellos con mayores ingresos. Promoveré programas de asistencia social efectivos y accesibles para quienes más lo necesitan. Además, buscaré aumentar el salario mínimo y mejorar las condiciones laborales para garantizar que todos los ciudadanos tengan la oportunidad de prosperar.",
            "boton1": "Para abordar la desigualdad de ingresos, considero importante implementar políticas que promuevan la igualdad de oportunidades. Esto implica la inversión en educación y capacitación para que las personas puedan acceder a empleos mejor remunerados. También abogaré por políticas que protejan los derechos de los trabajadores y promuevan un mercado laboral justo. Si bien la redistribución es importante, mi enfoque se centra en crear condiciones para que las personas mejoren sus ingresos a través del trabajo y la formación.",
            "boton0": "Creo que la desigualdad de ingresos es un problema que no debe ser abordado por el gobierno. En lugar de aumentar los impuestos o redistribuir la riqueza, promoveré políticas que fomenten la inversión y el emprendimiento. La libre competencia y la reducción de regulaciones permitirán que las personas creen sus propias oportunidades económicas. No creo en la intervención estatal en la economía como solución a la desigualdad de ingresos."
        },
        "respuestas_Massa": {
            "refute": "En mi visión, propongo un aumento de impuestos a los más ricos y la implementación de programas de redistribución de la riqueza para combatir la desigualdad.",
            "boton2": "Para abordar la desigualdad de ingresos, propongo implementar políticas sociales y económicas equitativas. Esto incluye la redistribución de la riqueza a través de impuestos progresivos para aquellos con mayores ingresos. Promoveré programas de asistencia social efectivos y accesibles para quienes más lo necesitan. Además, buscaré aumentar el salario mínimo y mejorar las condiciones laborales para garantizar que todos los ciudadanos tengan la oportunidad de prosperar.",
            "boton1": "Para abordar la desigualdad de ingresos, considero importante implementar políticas que promuevan la igualdad de oportunidades. Esto implica la inversión en educación y capacitación para que las personas puedan acceder a empleos mejor remunerados. También abogaré por políticas que protejan los derechos de los trabajadores y promuevan un mercado laboral justo. Si bien la redistribución es importante, mi enfoque se centra en crear condiciones para que las personas mejoren sus ingresos a través del trabajo y la formación.",
            "boton0": "Creo que la desigualdad de ingresos es un problema que no debe ser abordado por el gobierno. En lugar de aumentar los impuestos o redistribuir la riqueza, promoveré políticas que fomenten la inversión y el emprendimiento. La libre competencia y la reducción de regulaciones permitirán que las personas creen sus propias oportunidades económicas. No creo en la intervención estatal en la economía como solución a la desigualdad de ingresos."
        }
    },
    6: {
        "texto": "¿Qué políticas proponen los candidatos para mejorar la infraestructura y el transporte público?",
        "respuestas_Milei": {
            "refute": "Mi enfoque en la infraestructura es promover la inversión privada y la reducción de la intervención estatal en el transporte público.",
            "boton2": "Para mejorar la infraestructura y el transporte público, propongo un enfoque integral que incluya inversiones significativas en proyectos de infraestructura clave. Esto implicaría la expansión y modernización de la red de transporte público, así como la construcción y mantenimiento de carreteras, puentes y otras infraestructuras esenciales. Además, promoveré la inversión en sistemas de transporte sostenible y energéticamente eficientes para reducir la contaminación y mejorar la movilidad de las personas. Mi objetivo es crear una infraestructura de calidad que beneficie a todos los ciudadanos y fomente el crecimiento económico.",
            "boton1": "Para mejorar la infraestructura y el transporte público, considero importante fomentar la colaboración público-privada. Esto implica atraer inversiones del sector privado en proyectos de infraestructura clave, al tiempo que se mantiene un alto estándar de calidad y accesibilidad para los ciudadanos. Además, abogaré por la modernización de los sistemas de transporte público existentes y la promoción de soluciones de movilidad sostenible. Buscaré equilibrar la inversión pública y privada para garantizar que la infraestructura y el transporte sean eficientes y efectivos.",
            "boton0": "No creo que el gobierno deba desempeñar un papel activo en la mejora de la infraestructura y el transporte público. En cambio, fomentaré la inversión y la iniciativa privada en este ámbito. La competencia y la innovación del sector privado pueden llevar a soluciones más eficientes y rentables. Reduciré la burocracia y las regulaciones que obstaculizan la inversión privada en infraestructura y transporte. Mi enfoque es permitir que el mercado y la inversión privada impulsen la mejora de la infraestructura."
        },
        "respuestas_Massa": {
            "refute": "En mi visión, propongo una mayor inversión estatal en infraestructura y transporte público para mejorar la accesibilidad.",
            "boton2": "Para mejorar la infraestructura y el transporte público, propongo un enfoque integral que incluya inversiones significativas en proyectos de infraestructura clave. Esto implicaría la expansión y modernización de la red de transporte público, así como la construcción y mantenimiento de carreteras, puentes y otras infraestructuras esenciales. Además, promoveré la inversión en sistemas de transporte sostenible y energéticamente eficientes para reducir la contaminación y mejorar la movilidad de las personas. Mi objetivo es crear una infraestructura de calidad que beneficie a todos los ciudadanos y fomente el crecimiento económico.",
            "boton1": "Para mejorar la infraestructura y el transporte público, considero importante fomentar la colaboración público-privada. Esto implica atraer inversiones del sector privado en proyectos de infraestructura clave, al tiempo que se mantiene un alto estándar de calidad y accesibilidad para los ciudadanos. Además, abogaré por la modernización de los sistemas de transporte público existentes y la promoción de soluciones de movilidad sostenible. Buscaré equilibrar la inversión pública y privada para garantizar que la infraestructura y el transporte sean eficientes y efectivos.",
            "boton0": "No creo que el gobierno deba desempeñar un papel activo en la mejora de la infraestructura y el transporte público. En cambio, fomentaré la inversión y la iniciativa privada en este ámbito. La competencia y la innovación del sector privado pueden llevar a soluciones más eficientes y rentables. Reduciré la burocracia y las regulaciones que obstaculizan la inversión privada en infraestructura y transporte. Mi enfoque es permitir que el mercado y la inversión privada impulsen la mejora de la infraestructura."
        }
    },
    7: {
        "texto": "¿Cuál es la postura de cada candidato sobre la inmigración y las políticas de fronteras?",
        "respuestas_Milei": {
            "refute": "Abogaré por una política de inmigración que promueva la libertad individual y económica. Esto significa que, si bien Argentina debe mantener fronteras seguras, también debe ser un lugar acogedor para quienes buscan oportunidades y prosperidad. Implementaré un sistema en el que los extranjeros contribuyan al financiamiento de servicios como la salud y la educación, pero al mismo tiempo, eliminaré regulaciones que obstaculicen la entrada y la inversión extranjera en nuestro país. Mi enfoque se basa en la libertad y la responsabilidad individual.",
            "boton2": "Abogo por una política de inmigración que sea humanitaria y al mismo tiempo, garantice la seguridad de nuestro país. Creo en la importancia de acoger a personas que buscan refugio o mejores oportunidades en Argentina. Trabajaré para agilizar los procesos de solicitud de asilo y visas, al tiempo que implementaré medidas para garantizar la integración de los inmigrantes en nuestra sociedad. También abogaré por una mayor cooperación regional en cuestiones migratorias para abordar este desafío de manera conjunta.",
            "boton1": "Considero que debemos mantener un equilibrio entre ser acogedores con los inmigrantes y garantizar la seguridad de nuestras fronteras. Trabajaré para mejorar nuestros sistemas de control y seguimiento de inmigrantes, asegurando que aquellos que ingresan al país lo hagan de manera legal y segura. También promoveré programas de integración para ayudar a los inmigrantes a adaptarse a nuestra sociedad y contribuir a nuestra economía.",
            "boton0": "Creo que debemos ser más estrictos en cuanto a la inmigración y nuestras políticas de fronteras. Implementaré medidas más restrictivas para controlar y limitar la entrada de inmigrantes en el país. Esto incluirá controles más rigurosos en las fronteras y una reducción en los beneficios otorgados a los inmigrantes. Mi prioridad es la seguridad de Argentina, y creo que debemos ser más selectivos en cuanto a quiénes permitimos ingresar y establecerse en nuestro país."
        },
        "respuestas_Massa": {
            "refute": "Creo que debemos ser solidarios con aquellos que buscan refugio o una vida mejor en Argentina. Promoveré una política de inmigración humanitaria que ofrezca oportunidades a quienes lo necesitan. Trabajaré en estrecha colaboración con organizaciones internacionales y otros países para abordar de manera conjunta los desafíos migratorios. Mi enfoque es asegurarnos de que todos sean tratados con dignidad y respeto, y promover políticas de integración que permitan a los inmigrantes ser parte activa de nuestra sociedad.",
            "boton2": "Abogo por una política de inmigración que sea humanitaria y al mismo tiempo, garantice la seguridad de nuestro país. Creo en la importancia de acoger a personas que buscan refugio o mejores oportunidades en Argentina. Trabajaré para agilizar los procesos de solicitud de asilo y visas, al tiempo que implementaré medidas para garantizar la integración de los inmigrantes en nuestra sociedad. También abogaré por una mayor cooperación regional en cuestiones migratorias para abordar este desafío de manera conjunta.",
            "boton1": "Considero que debemos mantener un equilibrio entre ser acogedores con los inmigrantes y garantizar la seguridad de nuestras fronteras. Trabajaré para mejorar nuestros sistemas de control y seguimiento de inmigrantes, asegurando que aquellos que ingresan al país lo hagan de manera legal y segura. También promoveré programas de integración para ayudar a los inmigrantes a adaptarse a nuestra sociedad y contribuir a nuestra economía.",
            "boton0": "Creo que debemos ser más estrictos en cuanto a la inmigración y nuestras políticas de fronteras. Implementaré medidas más restrictivas para controlar y limitar la entrada de inmigrantes en el país. Esto incluirá controles más rigurosos en las fronteras y una reducción en los beneficios otorgados a los inmigrantes. Mi prioridad es la seguridad de Argentina, y creo que debemos ser más selectivos en cuanto a quiénes permitimos ingresar y establecerse en nuestro país."
        }
    },
    8: {
        "texto": "¿Cómo planean los candidatos fomentar la inversión extranjera y el comercio internacional?",
        "respuestas_Milei": {
            "refute": "Mi enfoque en la inversión extranjera es promover la apertura económica y la eliminación de barreras al comercio internacional para atraer inversión extranjera.",
            "boton2": "Mi enfoque para fomentar la inversión extranjera y el comercio internacional es buscar un equilibrio entre la apertura a la inversión extranjera y la protección de nuestros intereses nacionales. Trabajaré en estrecha colaboración con inversores internacionales y promoveré acuerdos comerciales justos que beneficien tanto a Argentina como a nuestros socios comerciales. Mi objetivo es atraer inversiones que impulsen la creación de empleo y el crecimiento económico sostenible.",
            "boton1": "Considero que es importante fomentar la inversión extranjera y el comercio internacional de manera responsable. Buscaré oportunidades para atraer inversión extranjera que contribuya al desarrollo de nuestra economía y la generación de empleo. Trabajaré para mantener relaciones comerciales sólidas con otros países y promoveré políticas que protejan nuestros intereses económicos y comerciales.",
            "boton0": "Mi enfoque difiere en gran medida de fomentar la inversión extranjera y el comercio internacional. Creo que debemos mantener un control más estricto sobre nuestras fronteras y recursos, limitando la entrada de inversión extranjera y reduciendo nuestras relaciones comerciales internacionales. Mi prioridad es proteger nuestros intereses nacionales y recursos, incluso si eso significa limitar la inversión extranjera."
        },
        "respuestas_Massa": {
            "refute": "En mi visión, propongo una mayor regulación en la inversión extranjera y restricciones para proteger nuestros intereses nacionales.",
            "boton2": "Mi enfoque para fomentar la inversión extranjera y el comercio internacional es buscar un equilibrio entre la apertura a la inversión extranjera y la protección de nuestros intereses nacionales. Trabajaré en estrecha colaboración con inversores internacionales y promoveré acuerdos comerciales justos que beneficien tanto a Argentina como a nuestros socios comerciales. Mi objetivo es atraer inversiones que impulsen la creación de empleo y el crecimiento económico sostenible.",
            "boton1": "Considero que es importante fomentar la inversión extranjera y el comercio internacional de manera responsable. Buscaré oportunidades para atraer inversión extranjera que contribuya al desarrollo de nuestra economía y la generación de empleo. Trabajaré para mantener relaciones comerciales sólidas con otros países y promoveré políticas que protejan nuestros intereses económicos y comerciales.",
            "boton0": "Mi enfoque difiere en gran medida de fomentar la inversión extranjera y el comercio internacional. Creo que debemos mantener un control más estricto sobre nuestras fronteras y recursos, limitando la entrada de inversión extranjera y reduciendo nuestras relaciones comerciales internacionales. Mi prioridad es proteger nuestros intereses nacionales y recursos, incluso si eso significa limitar la inversión extranjera."
        }
    },
    9: {
        "texto": "¿Cuáles son las estrategias de cada candidato para garantizar la transparencia y la lucha contra la corrupción en el gobierno?",
        "respuestas_Milei": {
            "refute": "Donde no hay Estado, no hay corrupción. Mi enfoque se basa en reducir drásticamente la intervención estatal en la economía y la sociedad. Creo que la mejor manera de combatir la corrupción es limitando el poder del gobierno y eliminando las regulaciones innecesarias. Promoveré la transparencia al reducir la burocracia y eliminar las oportunidades para la corrupción. Además, fomentaré la competencia en el sector público y privado para garantizar una gestión eficiente y responsable de los recursos públicos.",
            "boton2": "Mi compromiso con la transparencia y la lucha contra la corrupción es sólido. Trabajaré en estrecha colaboración con las instituciones de control y supervisión para garantizar la rendición de cuentas en el gobierno. Promoveré la implementación de medidas de transparencia, como la publicación de datos gubernamentales, y fortaleceré los mecanismos de investigación de la corrupción. Mi objetivo es crear un gobierno limpio y responsable que sirva a los intereses del pueblo.",
            "boton1": "La transparencia y la lucha contra la corrupción son fundamentales para un gobierno eficaz. Trabajaré para fortalecer las instituciones de control y supervisión, y promoveré la transparencia en la gestión gubernamental. Implementaré políticas para prevenir la corrupción y colaboraré con organizaciones de la sociedad civil y la comunidad internacional en la lucha contra la corrupción. Mi objetivo es mejorar la integridad del gobierno.",
            "boton0": "Tengo reservas sobre la efectividad de las medidas de transparencia y la lucha contra la corrupción en el gobierno. Considero que algunas de estas medidas pueden ser innecesarias y burocráticas. Mi enfoque principal es la eficiencia gubernamental, y creo que debemos centrarnos en la gestión efectiva más que en la regulación excesiva. Buscaré equilibrar la transparencia con la eficiencia."
        },
        "respuestas_Massa": {
            "refute": "La transparencia y la lucha contra la corrupción son valores fundamentales para mi gobierno. Trabajaré en estrecha colaboración con las instituciones de control y supervisión para garantizar la rendición de cuentas en el gobierno. Implementaré medidas de transparencia y promoveré la ética en la función pública. Además, fortaleceré los mecanismos de investigación de la corrupción y colaboraré con la sociedad civil y la comunidad internacional en esta lucha. Mi objetivo es construir un gobierno honesto y responsable que sirva a los intereses de la ciudadanía.",
            "boton2": "Mi compromiso con la transparencia y la lucha contra la corrupción es sólido. Trabajaré en estrecha colaboración con las instituciones de control y supervisión para garantizar la rendición de cuentas en el gobierno. Promoveré la implementación de medidas de transparencia, como la publicación de datos gubernamentales, y fortaleceré los mecanismos de investigación de la corrupción. Mi objetivo es crear un gobierno limpio y responsable que sirva a los intereses del pueblo.",
            "boton1": "La transparencia y la lucha contra la corrupción son fundamentales para un gobierno eficaz. Trabajaré para fortalecer las instituciones de control y supervisión, y promoveré la transparencia en la gestión gubernamental. Implementaré políticas para prevenir la corrupción y colaboraré con organizaciones de la sociedad civil y la comunidad internacional en la lucha contra la corrupción. Mi objetivo es mejorar la integridad del gobierno.",
            "boton0": "Tengo reservas sobre la efectividad de las medidas de transparencia y la lucha contra la corrupción en el gobierno. Considero que algunas de estas medidas pueden ser innecesarias y burocráticas. Mi enfoque principal es la eficiencia gubernamental, y creo que debemos centrarnos en la gestión efectiva más que en la regulación excesiva. Buscaré equilibrar la transparencia con la eficiencia."
        }
    },
    # Agrega más preguntas aquí
}
