

<template>
    <div class="wrapper">
        <page-logo/>
        <div class="search">
            <search-bar @query-submit="searchQuery" />
        </div>
    </div>
</template>


<script>
import SearchBar from '@/components/SearchBar.vue';
import PageLogo from '@/components/PageLogo.vue';

export default {
    components: { SearchBar, PageLogo },
    methods: {
        searchQuery(query){
            this.$router.push({ name: 'search', query: { query } });
        }
    }
}
</script>

<style scoped>

.wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    height: 98vh;
}

div.search {
    width: 50%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.page-logo {
    --height: 120px;
    /* --font-size: 5rem; */
}

</style>



