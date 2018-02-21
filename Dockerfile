FROM jruby:latest

ENV APP_HOME /mondrian-rest
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD . $APP_HOME
RUN bundle install
RUN jruby -G -S jbundle install

ENV JRUBY_OPTS="-G --server"
ENV JAVA_OPTS="-Dmondrian-rest.sparseDefault=true -Dmondrian.rolap.evaluate.MaxEvalDepth=100"

CMD ["puma", "config.ru", "-b", "tcp://0.0.0.0:9292", "-t", "8:32", "-e", "production"]

