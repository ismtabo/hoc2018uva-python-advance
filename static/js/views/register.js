const Register = {
	template: '#register-template',
	data() {
		return {
			username: '',
			password: '',
			check_password: ''
		}
	},
	methods: {
		register() {
			let username = this.username;
			let password = this.password;
			let check_password = this.check_password;
			this.$store.dispatch('register', { username, password, check_password })
				.then(() => this.$router.push('/'))
				.catch(err => console.error(error));
		}
	}
};