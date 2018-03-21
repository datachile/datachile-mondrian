# Datachile Mondrian

Es la implementación de la capa lógica usando [Mondrian REST](https://github.com/jazzido/mondrian-rest) para Datachile.

Contiene la configuración del esquema de cubos y provee el entrypoint REST de la API para consultas.

Documentación completa para crear un schema aquí: [Mondrian Schema](https://mondrian.pentaho.com/documentation/schema.php)

## Para desarrollo local
1. Instalar [JRuby](http://jruby.org). Usar [RVM](https://rvm.io/) es recomendado.
2. Instalar dependencias con `bundle install`
3. Duplicar `config.yaml.example` bajo el nombre `config.yaml` y completar los datos.
4. Correr server `JRUBY_OPTS=-G MONDRIAN_REST_CONF=`pwd`/config.yaml MONDRIAN_REST_SECRET=lala JAVA_OPTS="-Dlog4j.configuration=file:log4j.properties -Dmondrian.olap.SsasCompatibleNaming=true" rackup` 

## Conceptos básicos
* Estrella
* Cubes
* Dimensions
* Levels
* Members
* Properties
* Measures

## Ejemplo de cubo
...

## Tablas `fact_` y tablas `dim_`
...

## Dimensiones en tablas vs Dimensiones inline
...

## i18n
Repetir datos puede ser un detalle sin importancia en las tablas `dim_` dado que OLAP siempre hará agregaciones. Pero puede multiplicarse si se necesita multilenguaje. Es la única manera de hacerlo: tener las dimensiones -y sus niveles- en varios idiomas en campos separados. Se indica el campo dentro de cada `Level` utilizando `Annotations` y `Property`.

Ejemplo de `Dimension` inline sobre grados de discapacidad:

```xml
<Dimension foreignKey="disability_grade" name="Disability Grade">
  <Annotations>
    <Annotation name="es_element_caption">Grado de discapacidad</Annotation>
  </Annotations>

  <Hierarchy hasAll="true">
    <InlineTable alias="disability_grade">
      <ColumnDefs>
        <ColumnDef name="id" type="Numeric"/>
        <ColumnDef name="description" type="String"/>
        <ColumnDef name="es_description" type="String"/>
      </ColumnDefs>
      <Rows>
        <Row>
          <Value column="id">1</Value>
          <Value column="description">No disability</Value>
          <Value column="es_description">Sin discapacidad</Value>
        </Row>
        <Row>
          <Value column="id">2</Value>
          <Value column="description">Slight to moderate</Value>
          <Value column="es_description">Leve a moderada</Value>
        </Row>
        <Row>
          <Value column="id">3</Value>
          <Value column="description">Severe</Value>
          <Value column="es_description">Severa</Value>
        </Row>
      </Rows>
    </InlineTable>

    <Level column="id" name="Disability Grade" nameColumn="description" uniqueMembers="true">
      <Annotations>
        <Annotation name="es_caption">Description ES</Annotation>
      </Annotations>

      <Property column="es_description" name="Description ES"/>
    </Level>
  </Hierarchy>
</Dimension>
```

Luego en el query habrá que solicitar el `caption` al `drilldown` basado en el nombre de la `property.`
