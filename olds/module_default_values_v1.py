def serveData():
  """ Defining the default values """
  data = {}
  data["Frontend"] = []
  data["Frontend"].append({
      'id' : 'ttl',
      'value' : 'This is the app title'
  })
  data["Frontend"].append({
      'id' : 'hdr1',
      'value' : 'This is header 1'
  })
  data["Frontend"].append({
      'id' : 'lbl1',
      'value' : 'This is label 1'
  })
  data["Frontend"].append({
      'id' : 'lbl2',
      'value' : 'This is label 2'
  })
  data["Backend"] = []
  data["Backend"].append({
    'parameters' : {
      'id' : 'adEml',
      'value' : 'admin@email.com'
    }
  })
  return data