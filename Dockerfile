FROM jruby:latest

ENV APP_HOME /mondrian-rest
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD . $APP_HOME
RUN bundle install
RUN jruby -G -S jbundle install

ENV JRUBY_OPTS -G
ENV JAVA_OPTS="-Dmondrian-rest.sparseDefault=true"

CMD ["rackup", "-o", "0.0.0.0"]
