<template>
    <search-bar></search-bar>
    <main>
        <result-card v-for="obj of this.results" :key="obj.link" v-bind="obj" />
    </main>
</template>

<script>
import ResultCard from '@/components/ResultCard.vue';
import SearchBar from '../components/SearchBar.vue';
export default {
    components: {
    ResultCard,
    SearchBar
},
    data: () => ({
        results: [],
    }),
    created() {
        const backend = "http://localhost:8000/search";
        const query = this.$route.query.query;
        fetch(`${backend}?query=${query}`)
            .then((response) => {
                if (!response.ok) throw new Error("response was not ok");
                return response.json();
            })
            .then((results) => {
                this.results = results;
            })
            .catch(() => null);
    },
}
</script>

<style>
@media (min-width: 1024px) {
    .about {
        min-height: 100vh;
        display: flex;
        align-items: center;
    }
}
</style>
