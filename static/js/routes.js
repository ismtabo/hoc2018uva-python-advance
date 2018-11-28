const routes = [
	{ path: '/', component: Home, meta: { requiresAuth: true } },
	{ path: '/login', component: Login },
	{ path: '/register', component: Register }
]

const router = new VueRouter({
	routes
});

router.beforeEach((to, from, next) => {
	if (to.matched.some(record => record.meta.requiresAuth)) {
		if (store.getters.isLoggedIn) {
			next()
			return
		}
		next('/login')
	} else {
		next()
	}
});