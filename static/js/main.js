const socket = io();

function update_users(users) {
	document.getElementById('users').innerHTML = '' + users;
}

socket.on('new connection', function (data) {
	update_users(data.users);
});

socket.on('new disconnection', function (data) {
	update_users(data.users);
});

socket.on('new comment', function (data) {
	add_comment(data.comment);
})

function add_comment(comment) {
	let comment_list = document.getElementById('comment-list');
	let users_span = document.getElementById('users-span');

	let li = document.createElement('li');
	li.innerHTML = `<a href="#" class="comment list-group-item list-group-item-action flex-column align-items-start">
					<div class="d-flex w-100 justify-content-between">
						<h5 class="mb-1">${comment.title}</h5>
						<small class="mb-1">${comment.author}</small>
					</div>
					<p class="mb-1">${comment.content}</p>
					<div class="d-flex flex-row justify-content-end">
						<small class="mb-1">${moment(comment.datetime).fromNow()}</small>
					</div>
				</a>`;

	comment_list.insertBefore(li, users_span);
}