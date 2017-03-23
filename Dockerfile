FROM jruby:latest

ENV APP_HOME /mondrian-rest
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD . $APP_HOME
RUN bundle install

ENV JRUBY_OPTS -G

CMD ["rackup", "-o", "0.0.0.0"]
