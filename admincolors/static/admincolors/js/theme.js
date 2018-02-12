(function() {
    const oneYear = 1000 * 60 * 60 * 24 * 365
    document.querySelectorAll('[data-toggle="switch-theme"]').forEach(
        (el) => {
            el.onclick = () => {
                document.cookie = (
                    'theme=' + el.getAttribute('data-target') +
                    '; expires=' + new Date(
                        new Date().getTime() + oneYear
                    ).toUTCString() + ';'
                )
            }
        }
    )
})()
