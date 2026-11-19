void somas(int v[], int n, int ini[], int fim[], int q, long resp[]) {
    for (int k = 0; k < q; k++) {
        long s = 0;
        for (int i = 0; i < n; i++) {
            if (i >= ini[k] && i <= fim[k]) {
                s = s + v[i];
            }
        }
        resp[k] = s;
    }
}