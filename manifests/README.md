# How to properly create a PostgreSQL StatefulSet

## Sequence of Creating Resources

### Namespace

To begin, create a namespace:

```bash
  kubectl apply -f postgres-namespace
  ```

### ConfigMap and Secret

Apply the ConfigMap and Secret for PostgreSQL:

```bash
  kubectl apply -f postgres-configmap.yaml
    kubectl apply -f postgres-secret.yaml
    ```

### Service 

Apply the Service for PostgreSQL:

```bash
  kubect apply -f postgres-secret.yaml
  ```

### StatefulSet

Apply the StatefulSet for PostgreSQL:

```bash
  kubectl apply -f postgres-statefulset.yaml
  ```

## Access the 'postgres-0' Pod and Interact with the Database

To access the 'postgres-0' pod and interact with the database, use the following command:

```bash
  kubectl exec -it postgres-0 -n postgresql -- bash
  ```

### Inside the Pod

Once inside the pod, access the PostgreSQL database:

```bash
  psql --username=postgresqladmin postgresdb
  ```

### It's All Up to You!

Feel free to explore and interact with the database as needed.

## Deleting All Resources

To delete all resources, navigate to the 'Shop' directory and execute the following command:

```bash
  kubectl delete -f manifests/
  ```

