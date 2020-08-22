<template>
    <v-container>
        <v-row class="justify-center">
            <v-col sm="5" >
                <v-card>
                    <v-card-title class="primary white--text">
                        <span>Login Form</span>
                        <v-spacer></v-spacer>
                        <v-icon class="white--text">code</v-icon>
                    </v-card-title>
                    <!-- El contenido de la tarjeta -->
                    <v-form>
                        <v-container>
                            <v-row>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="person" label="Username" :rules="rules" hide-details="auto"></v-text-field>
                                </v-col>
                                <v-col sm="12">
                                    <v-text-field prepend-icon="lock" label="Password"></v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-form>
                    <!-- Los botones por ejemplo -->
                    <v-card-actions class="justify-end pt-0 pb-5">
                        <router-link to="/sign_up" class="mr-2"><v-btn color="secondary" rounded>SIGN UP</v-btn></router-link>
                        <v-btn color="info" rounded>LOG IN</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>