document.addEventListener('DOMContentLoaded', function () {
    // Sélectionner tous les boutons de catégorie
    var categoryButtons = document.querySelectorAll('.category-button');

    // Ajouter un gestionnaire d'événements à chaque bouton de catégorie
    categoryButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var categoryId = button.getAttribute('data-category-id');
            fetchProducts(categoryId);
        });
    });
});

var staticMediaPath = "";

function fetchProducts(categoryId) {
    fetch('/filtered_products/' + categoryId + '/')
        .then(function (response) {
            if (!response.ok) {
                throw new Error('Error fetching products: ' + response.statusText);
            }
            return response.json();
        })
        .then(function (data) {
            updateProductSection(data.products);
        })
        .catch(function (error) {
            console.error('Error fetching products:', error);
        });
}

function updateProductSection(products) {
    // Supprimer les anciens produits de la section
    var productsWrapper = document.getElementById('products-wrapper');
    productsWrapper.innerHTML = '';

    // Traiter chaque produit
    products.forEach(function (product) {
        // Créer des éléments HTML pour chaque produit 
        var productElement = document.createElement('article');
        productElement.classList.add('article-cell');

        var ulElement = document.createElement('ul');
        var liElement = document.createElement('li');

        // Vérifier si la propriété 'discount' existe et si elle est définie
        var hasDiscount = product.discount && typeof product.discount === 'object' && product.discount.active;

        if (hasDiscount) {
            liElement.classList.add('discount-active');
        }

        var h3Element = document.createElement('h3');
        h3Element.classList.add('name');
        h3Element.textContent = product.name;

        var pElement = document.createElement('p');
        pElement.classList.add('description');
        pElement.textContent = product.description;

        var initPriceElement = document.createElement('span');
        initPriceElement.classList.add('init-price');
        initPriceElement.textContent = product.initial_price + ' €';

        liElement.appendChild(h3Element);
        liElement.appendChild(pElement);
        liElement.appendChild(initPriceElement);

        if (hasDiscount) {
            var discountPriceElement = document.createElement('span');
            discountPriceElement.classList.add('discount-price');
            discountPriceElement.textContent = product.discount.discounted_price + ' €';

            var offerElement = document.createElement('span');
            offerElement.classList.add('offer');
            offerElement.textContent = product.discount.discount_percentage + ' % off';

            liElement.appendChild(discountPriceElement);
            liElement.appendChild(offerElement);
        }
        // Vérifier si image et l'afficher
        if (product.thumbnail_url) {
            var imgElement = document.createElement('img');
            imgElement.classList.add('product-img');
            imgElement.src = staticMediaPath + product.thumbnail_url;
            imgElement.alt = 'A picture of ' + product.name;

            liElement.appendChild(imgElement);
        }

        ulElement.appendChild(liElement);
        productElement.appendChild(ulElement);
        productsWrapper.appendChild(productElement);
    });
}
