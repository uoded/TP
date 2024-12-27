### Différences entre tests unitaires, tests d'intégration et tests end-to-end

#### 1. **Test unitaire** (Unit Test)
- **Objectif** : Tester une unité isolée de code (comme une fonction, une méthode ou une classe).
- **Caractéristiques** :
  - Très rapides à exécuter.
  - Pas de dépendances externes (mocking utilisé pour simuler les interactions).
  - Isolés des autres parties du système.
- **Exemple** : Tester si une fonction `add_numbers(a, b)` retourne correctement la somme de `a` et `b`.

#### 2. **Test d'intégration** (Integration Test)
- **Objectif** : Vérifier si plusieurs modules ou composants fonctionnent correctement ensemble.
- **Caractéristiques** :
  - Teste les interactions entre différents services, bases de données, API, etc.
  - Peut impliquer des configurations complexes (bases de données de test, fichiers externes simulés, etc.).
  - Plus lents que les tests unitaires.
- **Exemple** : Tester si une API REST renvoie les données attendues après avoir consulté une base de données.

#### 3. **Test end-to-end (E2E)**
- **Objectif** : Tester le système complet, du début à la fin, dans des conditions proches de la réalité.
- **Caractéristiques** :
  - Reproduit des scénarios utilisateurs réels.
  - Teste l'application dans son intégralité (front-end, back-end, bases de données, etc.).
  - Très lents par rapport aux autres types de tests.
- **Exemple** : Tester si un utilisateur peut se connecter, voir son tableau de bord et effectuer une action comme l'ajout d'un article au panier.

---

### Différences entre TDD et BDD

#### 1. **TDD (Test-Driven Development)** : Développement piloté par les tests
- **Concept** :
  - Écrire les tests unitaires **avant** d’écrire le code de production.
  - Cycle : **Échec** → **Code** → **Succès** (Red-Green-Refactor).
- **Focus** :
  - Basé sur les **unités de code**.
  - Orienté développeur.
- **Étapes** :
  1. Écrire un test qui échoue.
  2. Écrire le code minimum pour passer le test.
  3. Réfactorer le code si nécessaire.
- **Exemple** : 
  - Écrire un test pour vérifier que `add_numbers(2, 3)` retourne `5`, puis écrire la fonction.

#### 2. **BDD (Behavior-Driven Development)** : Développement piloté par le comportement
- **Concept** :
  - Basé sur des **scénarios métiers** rédigés en langage naturel (souvent en Gherkin avec `Given`, `When`, `Then`).
  - Orienté collaboration entre développeurs, testeurs et équipes métiers.
- **Focus** :
  - Basé sur le **comportement attendu**.
  - Couvre à la fois les tests d'intégration et les tests end-to-end.
- **Exemple** : 
  - Scénario :
    ```gherkin
    Given un utilisateur sur la page de connexion
    When il entre des identifiants valides
    Then il est redirigé vers le tableau de bord.
    ```

---

### Résumé des différences

| **Aspect**              | **TDD**                                 | **BDD**                                |
|-------------------------|-----------------------------------------|---------------------------------------|
| **Focus**               | Tests techniques sur le code           | Comportement fonctionnel de l'application |
| **Cible**               | Développeurs                           | Développeurs, testeurs, métier         |
| **Langage**             | Langage de programmation               | Langage naturel (Gherkin, etc.)       |
| **Type de test**        | Tests unitaires                        | Tests fonctionnels et end-to-end      |
| **Documentation**       | Peu générée                            | Documentation vivante à partir des scénarios |
| **Exemple**             | Vérifier qu'une fonction retourne la bonne valeur | Vérifier que l'utilisateur peut effectuer une action complète |

--- 

### Utilisation conjointe
- **TDD** : Pour s'assurer que chaque unité de code fonctionne comme prévu.
- **BDD** : Pour garantir que les fonctionnalités globales respectent les exigences métier.