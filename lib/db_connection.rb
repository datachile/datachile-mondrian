def db_connection(conf_yaml_path)
  YAML.load_file(conf_yaml_path)
end
