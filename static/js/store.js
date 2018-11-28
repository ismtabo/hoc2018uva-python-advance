Vue.config.devtools = true;

Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		status: '',
		token: localStorage.getItem('token') || '',
		user: JSON.parse(localStorage.getItem('user') || '{}')
	},
	mutations: {
		auth_request(state) {
			state.status = 'loading'
		},
		auth_success(state, payload) {
			state.status = 'success'
			state.token = payload.token
			state.user = payload.user
		},
		auth_error(state) {
			state.status = 'error'
		},
		logout(state) {
			state.status = ''
			state.token = ''
		},
	},
	actions: {
		login({ commit }, _user) {
			return new Promise((resolve, reject) => {
				commit('auth_request');
				axios({ url: '/auth/login', data: _user, method: 'POST' })
					.then(resp => {
						const token = resp.data.token;
						const user = resp.data.user;
						localStorage.setItem('token', token);
						localStorage.setItem('user', JSON.stringify(user));
						axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
						commit('auth_success', {token, user});
						resolve(resp);
					})
					.catch(err => {
						commit('auth_error');
						localStorage.removeItem('token');
						reject(err);
					});
			})
		},
		register({ commit }, user) {
			return new Promise((resolve, reject) => {
				commit('auth_request')
				axios({ url: '/auth/register', data: user, method: 'POST' })
					.then(resp => {
						const token = resp.data.token;
						const user = resp.data.user;
						localStorage.setItem('token', token);
						localStorage.setItem('user', JSON.stringify(user));
						axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
						commit('auth_success', {token, user});
						resolve(resp);
					})
					.catch(err => {
						commit('auth_error', err);
						localStorage.removeItem('token');
						reject(err);
					})
			})
		},
		logout({ commit }) {
			return new Promise((resolve, reject) => {
				commit('logout');
				axios({ url: '/auth/logout', method: 'POST' })
					.then(() => {
						localStorage.removeItem('token');
						delete axios.defaults.headers.common['Authorization'];
						resolve();
					})
					.catch(err => {
						commit('auth_error', err);
						console.error(err);
						reject(err);
					})
			})
		}
	},
	getters: {
		isLoggedIn: state => !!state.token,
		authStatus: state => state.status,
		user: state => state.user
	}
})