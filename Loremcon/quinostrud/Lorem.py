def init():
  """Initializes the module."""

  global _CLIENT
  _CLIENT = googleapiclient.discovery.build(
      'compute', 'v1',
      cache_discovery=False,
      developerKey=GOOGLE_DEVELOPER_KEY)
