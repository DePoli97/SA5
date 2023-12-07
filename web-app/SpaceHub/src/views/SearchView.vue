<template>
      <page-logo />
      <div class="search">
        <search-bar :initial_query="this.$route.query.query" @query-submit="searchQuery" />
        <div class="buttons">

          <button @click="previousPage" :disabled="!previousAvailable">prev</button>
          <button style="margin-right: 2%" @click="nextPage" :disabled="!nextAvailable">next</button>
        </div>
      </div>
    <main>
        <h3 v-if="this.results.length == 0"> No results found for this query</h3>
        <div style="display: flex; margin: 2%">
          <div style="flex:70%">
            <result-card v-for="obj of this.pageResults" :key="obj.link" v-bind="obj" v-model:vote="votes[obj.i]" />
          </div>
          <div style="flex:30%">
<!--              other suggestions-->
          </div>
        </div>
    </main>
</template>

<script>
import ResultCard from '@/components/ResultCard.vue';
import SearchBar from '@/components/SearchBar.vue';
import PageLogo from '@/components/PageLogo.vue';

export default {
    components: {
        ResultCard,
        SearchBar,
        PageLogo
    },
    data: () => ({
        results: [],
        page: 0,
        resultsPerPage: 10,
        votes: Array(100).fill(0)
    }),
    computed: {
        pageResults() {
            return this.results.slice(
                this.page * this.resultsPerPage,
                (this.page + 1) * this.resultsPerPage
            );
        },
        previousAvailable() { return this.results.length > 0 && this.page > 0 },
        nextAvailable() { return this.results.length > 0 && this.page < Math.floor(this.results.length / this.resultsPerPage) },
    },
    watch: {
        votes: {
            handler() {
                // console.log(this.votes);
            },
            deep: true,
        }
    },
    methods: {
        previousPage() { this.page -= this.previousAvailable },
        nextPage() { this.page += this.nextAvailable },
        searchQuery(query) {
            const backend = "http://localhost:8000/search";
            fetch(`${backend}?query=${query}`,
                {
                    method: "POST"
                    , headers: {
                        "Content-Type": "application/json",
                    }
                    , body: JSON.stringify({feedback : this.votes})
                })
                .then((response) => {
                    if (!response.ok) throw new Error("Response was not ok");
                    return response.json();
                })
                .then((results) => {
                    this.results = results.map((obj, i) => Object.assign(obj, { i }));
                    this.votes = Array(results.length).fill(0);
                })
                .catch(() => null);
            this.$router.push({ name: 'search', query: { query } });
        },
    },
    created() {
        const query = this.$route.query.query;
        this.searchQuery(query);
    },
}
</script>

<style scoped>
button {
    font-size: 1.5em;
    color: #f4f4f4;
    border: 1px solid red;
    border-radius: 8px;
    background-color: #1a1a26;
}

button:disabled {
    color: #777777;
    border: 1px solid #663300;
}


div.search {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 5px;
}

.buttons {
    display: grid;
    grid-template-columns: repeat(2, 200px);
    column-gap: 5px;
}

main {
    margin-top: 2em;
}

.page-logo {
    --height: 60px;
}
</style>
