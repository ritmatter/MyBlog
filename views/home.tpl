<h2>Home</h2>
%if posts.count() == 0:
   <p>Oops!  There are no blog posts to show right now!</p>
%end

% for post in posts :
   <h3>{{post["title"]}}</h3>
   <p>{{post["date"]}}</p>
   % import html2text 
   % content = unicode(post["content"])
   % content = content.encode('ascii', 'xmlcharrefreplace')
   % print content
   <html>{{post["content"]}}</html>
% end
%rebase base posts=posts
