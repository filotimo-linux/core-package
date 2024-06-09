set MODULE="nvidia"
if (`lsmod | grep -wq "$MODULE"`) then
    setenv LIBVA_DRIVER_NAME "nvidia"
    setenv MOZ_DISABLE_RDD_SANDBOX 1
    setenv EGL_PLATFORM "$XDG_SESSION_TYPE"
endif
