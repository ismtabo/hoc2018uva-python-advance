
const Home = {
	template: '#home-template',
	delimiters: ["[[", "]]"],
	data() {
		return {
			users: 0,
			comments: [],
			title: "",
			content: "",
			socket: null
		}
	},
	created() {
		this.socket = io();

		axios.get("/comments").then((response) => {
			this.comments = response.data.comments;
		}).catch((error) => {
			console.error(error);
		});

		this.socket.on("new connection", (data) => {
			this.users = data.users;
		});

		this.socket.on("new disconnection", (data) => {
			this.users = data.users;
		});

		this.socket.on("new comment", (data) => {
			this.comments.push(data.comment);
		});
	},
	destroyed() {
		this.socket.close();
	},
	methods: {
		onSubmitComment(event) {
			axios.post("/comments", {
				author: this.user.username,
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
			this.title = '';
			this.content = '';
		}
	},
	computed: {
		user() { return this.$store.getters.user }
	}
};
