<h2>Post!</h2>
<p>Hey {{name}}!  Put up some content!</p>

<form action="/posted" method="post">
	<div>
		<input name="title" type="text" placeholder="title" size="50" maxlength="500"/>
		<input name="date" type="text" placeholder="date" size="50" maxlength="500"/>
		<textarea name="content" placeholder="content" rows="30" cols="80"></textarea>
	</div>
	<div>
		<input type="submit" name="submit" value="Post!" />
	</div>
</form>
%rebase base
