Vue.config.devtools = true;

Vue.prototype.$http = axios;
const token = localStorage.getItem('token');
if (token) {
	Vue.prototype.$http.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

new Vue({
	router,
	store,
	delimiters: ["[[", "]]"],
	computed: {
		isLoggedIn: function () { return this.$store.getters.isLoggedIn }
	},
	methods: {
		logout() {
			this.$store.dispatch('logout')
				.then(() => {
					this.$router.push('/login')
				}).catch(err => console.error(err));
		}
	},
	created: function () {
		this.$http.interceptors.response.use(undefined, function (err) {
			return new Promise(function (resolve, reject) {
				if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
					this.$store.dispatch(logout)
				}
				throw err;
			});
		});
	}
}).$mount('#app');
