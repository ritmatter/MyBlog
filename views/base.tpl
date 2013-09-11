<html lang="en">
	<head>
      <meta charset="UTF-8">
		<title>My Blog</title>
		<link rel="stylesheet" type="text/css" href="/static/style.css"/>
	</head>
	<body id="blog_wrapper">
		<div id="container">
   		<div class="headerDiv">
            <ul>
               <div class="toptitle"><h1>My Blog</h1><p>Assorted Topics From the One and Only</p></div>
               <li class="headerLink"><a href="/">Home</a><li>
               <li class="headerLink"><a href="/posts">Posts</a></li>
               <li class="headerLink"><a href="/about">About</a></li>
               <li class="headerLink"><a href="/contact">Contact</a></li>
            </ul>
            <div class="clear"></div>
   			</div>
   			<div class="middle">
   				% include
   			</div>
   			<div class="footerDiv">
   				<p>Powered by MongoDB, Pymongo, and Bottle</p>
   			</div>
		</div>
      <div class="sidebar">
         % i = 0;
         % print "About to start loop"
         % for post in posts:
         %    print "Entering loop!"
         %    if i < 3:
                  <p>{{post["title"]}}</p><p>{{post["date"]}}</p>
         %        i += 1
         $        print i
         %     else :
         %        break
         %     end
         % end

      </div>
	</body>
</html>
