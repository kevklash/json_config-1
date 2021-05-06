def serveDataFR():
  """ Defining the default values for the backend config file """
  data = {}
  json_data = [
    {
        "id": "title",
        "value": "Gestion boîte de courriel"
    },
    {
        "id": "description",
        "value": "Cet outil est destiné à fournir des détails sur une boîte de courriel des clients à des fins d'interrogation et de recherche seulement, ainsi que d'aider avec quelques problèmes de connexion. Il peut fournir des indications concernant l'état du compte, les alias, les mécanismes de sécurité en cours d'utilisation, et l'utilisation de la boîte de courriel, y compris l'utilisation potentielle des applications tierces (POP / IMAP). Vous pouvez également supprimer toutes les informations supplémentaire de récupération pour les utilisateurs qui ont jamais été en mesure de s'authentifier, réinitialisation dans les cookies et réactiver un compte qui a été suspendu."
    },
    {
        "id": "input_label",
        "value": "Entrez l'adresse de courriel que vous souhaitez rechercher:"
    },
    {
        "id": "input_placeholder",
        "value": "Entrez une adresse e-mail s'il vous plaît"
    },
    {
        "id": "search_button",
        "value": "Chercher"
    },
    {
        "id": "not_found_confirm",
        "value": "Utilisateur non trouvé"
    },
    {
        "id": "not_found_info",
        "value": "Impossible de trouver des utilisateurs actifs avec cette adresse de courriel dans le courriel de TELUS fourni par Google"
    },
    {
        "id": "not_telus_confirm",
        "value": "Pas une entrée valide"
    },
    {
        "id": "not_telus_info",
        "value": "S'il vous plaît inclure un domaine supporté par TELUS"
    },
    {
        "id": "error_confirm",
        "value": "Erreur du serveur"
    },
    {
        "id": "error_info",
        "value": "Le serveur semble être en panne"
    },
    {
        "id": "header_1",
        "value": "informations de compte Google"
    },
    {
        "id": "rec_email_none",
        "value": "Rien"
    },
    {
        "id": "rec_phone_none",
        "value": "Rien"
    },
    {
        "id": "login_time",
        "value": "à"
    },
    {
        "id": "login_time_none",
        "value": "Ne s'est pas connecté"
    },
    {
        "id": "two_step",
        "value": "OUI"
    },
    {
        "id": "two_step_no",
        "value": "NON"
    },
    {
        "id": "two_step_tip",
        "value": "Cliquez ici pour en savoir plus sur la validation en deux étapes"
    },
    {
        "id": "suspended",
        "value": "OUI"
    },
    {
        "id": "not_suspended",
        "value": "NON"
    },
    {
        "id": "header_2",
        "value": "Actions"
    },
    {
        "id": "warning_1",
        "value": "Soyez conscient que ces actions affectera le compte du client. S'il vous plaît, utilisez avec précaution."
    },
    {
        "id": "warning_2",
        "value": "Aucun avertissement de suspension."
    },
    {
        "id": "warning_3",
        "value": "AVERTISSEMENT: la raison de la suspension indique que cet utilisateur peut être suspendu pour des raisons de facturation. La relance de la suspension ne résoudra pas le problème tant que la facturation ne sera pas corrigée. Veuillez confirmer ces informations avant de remettre la suspension."
    },
    {
        "id": "confirm_button",
        "value": "Confirmer"
    },
    {
        "id": "yes_button",
        "value": "Oui"
    },
    {
        "id": "no_button",
        "value": "Annuler"
    },
    {
        "id": "unsuspend_button",
        "value": "RÉACTIVER UTILISATEUR"
    },
    {
        "id": "unsuspend_on",
        "value": "Réactiver utilisateur"
    },
    {
        "id": "unsuspend_off",
        "value": "Puisque l'utilisateur n'est pas suspendu, ce bouton est désactivé"
    },
    {
        "id": "unsuspend_confirm",
        "value": "Annuler la suspension de l'utilisateur?"
    },
    {
        "id": "unsuspend_info",
        "value": "Vous êtes sur le point de passer outre l'état de suspension de cet utilisateur. Cela réactiver le compte dans le back-end.."
    },
    {
        "id": "unsuspend_success",
        "value": "L'utilisateur a été restauré avec succès"
    },
    {
        "id": "cancel_confirm",
        "value": "Annuler"
    },
    {
        "id": "cancel_info",
        "value": "Pas de changements"
    },
    {
        "id": "recovery_button",
        "value": "SUPPRIMER LES INFORMATIONS DE RÉCUPÉRATION"
    },
    {
        "id": "recovery_on",
        "value": "Supprimer les informations de récupération"
    },
    {
        "id": "recovery_off",
        "value": "Étant donné que cet utilisateur ne dispose d'aucune information de récupération, ce bouton est désactivé"
    },
    {
        "id": "recovery_confirm",
        "value": "Supprimer les informations de récupération?"
    },
    {
        "id": "recovery_info",
        "value": "Cela permettra d'éliminer à la fois l'e-mail de récupération et le numéro de téléphone de récupération dans le compte. Si leur demande de vérifier leur identité à ce moment, il les fera demander un numéro de téléphone portable pour recevoir un code. Dans le cas contraire, ils devront mettre à jour leurs informations de récupération sur myaccount.google.com pour éviter des problèmes à l'avenir."
    },
    {
        "id": "recovery_success",
        "value": "Les informations de récupération ont été supprimées avec succès"
    },
    {
        "id": "cookies_button",
        "value": "SIGN-IN RÉINITIALISER LES COOKIES"
    },
    {
        "id": "cookies_confirm",
        "value": "sign-in Réinitialiser les cookies?"
    },
    {
        "id": "cookies_info",
        "value": "Cette action obligera l'utilisateur à se déconnecter de toutes ses sessions actives. Pour ce faire, ils doivent entrer leur nom d'utilisateur et leur mot de passe pour se reconnecter à leur compte."
    },
    {
        "id": "cookies_success",
        "value": "Les cookies ont été réinitialisés avec succès"
    },
    {
        "id": "header_3",
        "value": "Changé par"
    },
    {
        "id": "header_4",
        "value": "email affectée"
    },
    {
        "id": "header_5",
        "value": "Événement"
    },
    {
        "id": "header_6",
        "value": "Date"
    },
    {
        "id": "header_7",
        "value": "IP"
    },
    {
        "id": "header_8",
        "value": "Self?"
    }
  ]


  for item in range(len(json_data)):
    data[json_data[item]["id"]] = json_data[item]["value"]
    

  return data