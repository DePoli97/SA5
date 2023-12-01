<template>
    <header class="page-logo">
        <a href="http://localhost:5173/">
            <h1>SPACE HUB</h1><img src="/public/favicon.ico" alt="logo">
        </a>
    </header>
</template>

<script>
</script>


<style scoped>
header {
    padding: 10px;
    position: relative;
    height: var(--height);
}

a {
    display: flex;
    gap:10px;
    text-decoration: none;
    font-size: 100%;
    height: 100%;
}

h1 {
    display: flex;
    align-items: center;
    font-size: calc(0.7 * var(--height));
}

img {
    max-height: 100%;
}
</style>