import os
import time

def get_article(x):
  dir = os.getcwd()[:-25]
  id = int(x)
  write_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(id))
  with open(dir + '\\%d'%id, 'r', encoding="utf-8") as article_file:
    title = article_file.readline()
    article = ''
    if title[0] == '《' and title[-2] == '》':
      article = article_file.readline()
      title = title[:-1]
    else:
      article = title
      title = x
    article = '写作时间：' + write_time + '<br>' + article
    return r'''
<div class="panel panel-default">
<div class="panel-heading">
<a data-toggle="collapse" data-parent="#accordion" href="#collapse''' + x + r'''">
<h4 class="panel-title">
'''+title+r'''
</h4>
</a>
</div>
<div id="collapse''' + x + r'''" class="panel-collapse collapse">
<h4 class="panel-body">
'''+article+r'''
</h4>
</div>
</div>

'''

def get_articles():
  dir = os.listdir(os.getcwd()[:-25])
  result = ''
  for i in dir:
    if i.isalnum():
      result = get_article(i) + result
  return result

s=(r'''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"> 
<title>Articles</title>
<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">  
<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
<link rel="icon" type="image/png" sizes="192x192"  href="https://cdn.freeriderhd.com/free_rider_hd/favicons/03282018/android-icon-192x192.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://cdn.freeriderhd.com/free_rider_hd/favicons/03282018/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="96x96" href="https://cdn.freeriderhd.com/free_rider_hd/favicons/03282018/favicon-96x96.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://cdn.freeriderhd.com/free_rider_hd/favicons/03282018/favicon-16x16.png">
</head>
<body>

<div class="jumbotron text-center" style="margin-bottom:0">
  <h1>Articles</h1>
</div>

<br>
<br>

<div class="container">
<div class="row">
<div class="col-sm-12">
<div class="panel-group" id="accordion">

''')+get_articles()+(r'''

</div>
</div>
</div>
</div>
</body>
</html>
''')
with open('index.html', 'w', encoding="utf-8") as ind:
  ind.write(s)