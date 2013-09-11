<h2>Posts</h2>
%if posts.count() == 0:
   <p>Oops!  There are no blog posts to show right now! POSTS PAGE!</p>
%else :
   <p>There are some blog posts!</p>
%end
%rebase base
