# Analysis Example
# Hello World

# Learn how to send messages to the console located on the TagoIO analysis screen.
# You can use this principle to show any information during and after development.

from tago import Analysis

# The function myAnalysis will run when you execute your analysis
def myAnalysis(context, scope):
  # This will log "Hello World" at the TagoIO Analysis console
  context.log("Hello World")

  #  This will log the environment to the TagoIO Analysis console
  context.log('Environment:', context.environment)

  #  This will log the scope to the TagoIO Analysis console
  context.log('my scope:', scope)

# The analysis token in only necessary to run the analysis outside TagoIO
Analysis('5534a049-755c-44d4-9030-6b5ebb0a5f7e').init(myAnalysis)