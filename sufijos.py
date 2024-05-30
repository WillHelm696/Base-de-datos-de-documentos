
def remove_suffixes(words):
  sufijos = [
    'aceo', 'acea', 'aco', 'aca', 'ada', 'ado', 'ada', 'aje', 'al', 'algia', 'amen', 
    'ancia', 'ano', 'ana', 'anza', 'ar', 'ario', 'aria', 'arquia', 'ata', 'ato', 'avo', 
    'ava', 'azgo', 'azo', 'bilidad', 'ble', 'cardio', 'cardia', 'cida', 'cidio', 'cion', 
    'cola', 'cracia', 'crata', 'cultor', 'cultora', 'dad', 'demia', 'dero', 'dera', 'dizo', 
    'diza', 'dor', 'dora', 'dura', 'ear', 'ecer', 'eco', 'edo', 'eda', 'edro', 'ego', 'ega', 
    'encia', 'eno', 'ena', 'ense', 'eno', 'ena', 'era', 'eria', 'ero', 'era', 'es', 'esa', 
    'esco', 'esca', 'ez', 'eza', 'fagia', 'fago', 'faga', 'fero', 'fera', 'filia', 'filo', 
    'fila', 'fito', 'fobia', 'fobo', 'foba', 'fono', 'fona', 'fonia', 'forme', 'fugo', 
    'fuga', 'gamia', 'gamo', 'gama', 'genia', 'geno', 'gena', 'geo', 'ginia', 'gino', 
    'gina', 'gono', 'grafia', 'grafo', 'grafa', 'grama', 'i', 'ia', 'iano', 'iana', 'ica', 
    'ido', 'ida', 'ificar', 'il', 'in', 'ina', 'ina', 'ing', 'ismo', 'ista', 'istico', 
    'istica', 'itis', 'izar', 'izo', 'iza', 'ita', 'latra', 'latria', 'lisis', 'lito', 
    'logia', 'logo', 'loga', 'illos', 'mancia', 'mania', 'mano', 'mana', 'mante', 'mente', 
    'mento', 'metria', 'metro', 'miento', 'nomia', 'nomo', 'noma', 'nte', 'oide', 'oleo', 
    'oma', 'ope', 'opia', 'osis', 'oso', 'osa', 'on', 'ona', 'or', 'pata', 'patia', 
    'pedia', 'podo', 'polis', 'teca', 'torio', 'tud', 'udo', 'uda', 'ura', 'ucho', 
    'ucha', 'voro', 'vora'
  ]
  
  for word in words:
    for suffix in sufijos:
      if word.endswith(suffix):
        word=re.sub(f'{suffix}$', '', word)
  return words
