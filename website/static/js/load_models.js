document.addEventListener("DOMContentLoaded", function() {
    const experienceField = document.querySelector('#id_experience');
    const modelField = document.querySelector('#id_model');

    experienceField.addEventListener('change', function() {
        const experienceId = this.value;

        fetch(`/ajax/load-models/?experience=${experienceId}`)
            .then(response => response.json())
            .then(data => {
                modelField.innerHTML = '';
                data.forEach(model => {
                    const option = document.createElement('option');
                    option.value = model.id;
                    option.textContent = model.libelle;
                    modelField.appendChild(option);
                });
            });
    });
});