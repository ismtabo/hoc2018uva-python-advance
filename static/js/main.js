const socket = io();

Vue.config.devtools = true;

var app = new Vue({
	el: "#app",
	delimiters: ["[[", "]]"],
	data: {
		users: 0,
		comments: [],
		author: "",
		title: "",
		content: ""
	},
	created() {
		axios.get("/comments", {
			author: document.getElementById("author").value,
			title: document.getElementById("title").value,
			content: document.getElementById("content").value
		}).then((response) => {
			this.comments = response.data.comments;
		}).catch((error) => {
			console.error(error);
		});

		socket.on("new connection", (data) => {
			this.users = data.users;
		});

		socket.on("new disconnection", (data) => {
			this.users = data.users;
		});

		socket.on("new comment", (data) => {
			this.comments.push(data.comment);
		});
	},
	methods: {
		onSubmitComment(event) {
			axios.post("/comments", {
				author: this.author,
				title: this.title,
				content: this.content
			}).then(() => {
				this.resetForm();
				event.target.reset();
				toastr.success("Your comment has been submited.", "Great!", {
					timeOut: 5000
				});
			}).catch((error) => {
				toastr.error("Your comment has not been submited.", "Warning!", {
					timeOut: 5000
				});
				console.error(error);
			});

		},
		resetForm() {
			this.author = '';
			this.title = '';
			this.content = '';
		}
	}
});
