<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <div class="wrapper">
        <header>
            <a href="http://localhost:5173/">
                <h1>SPACE HUB</h1>
            </a>
        </header>
        <RouterView />
    </div>
</template>

<style scoped>
.wrapper {
    display: flex;
    flex-direction: column;
    /* align-items: center;
    justify-content: center;
    place-items: center; */
}

header {
    line-height: 1.5;
    max-height: 100vh;
}

.logo {
    display: block;
    margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
    header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
        margin: 0 2rem 0 0;
    }


    nav {
        text-align: left;
        margin-left: -1rem;
        font-size: 1rem;

        padding: 1rem 0;
        margin-top: 1rem;
    }
}
</style>
