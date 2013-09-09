<h2>Home</h2>
%if posts.count() == 0:
   <p>Oops!  There are no blog posts to show right now!</p>
%else :
   <p>There are {{posts.count()}} blog posts!</p>
%end

% for post in posts :
   <h3>{{post["title"]}}</h3>
   <p>{{post["date"]}}</p> 
% end
%rebase base
