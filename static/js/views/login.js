const Login = {
	template: '#login-template',
	data() {
		return {
			username: '',
			password: ''
		}
	},
	methods: {
		login() {
			let username = this.username;
			let password = this.password;
			this.$store.dispatch('login', { username, password })
				.then(() => this.$router.push('/'))
				.catch(err => console.error(err));
		}
	}
};