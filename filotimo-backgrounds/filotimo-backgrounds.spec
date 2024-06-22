Name:           filotimo-backgrounds
Version:        0.1
Release:        1%{?dist}
Summary:        Wallpapers for Filotimo
License:        GPLv2+
URL:            https://github.com/filotimo-linux/filotimo-core-packages

Source0:        LICENSE
Source1:        ColdDunes.jpg
Source2:        Dawn.jpg
Source3:        Dunes.jpg
Source4:        FirstSnow.jpg
Source5:        HillsandMountains.jpg
Source6:        InClouds.jpg
Source7:        Kiss.jpg
Source8:        PinkHat.jpg
Source9:        MountainLanterns.jpg
Source10:       Obelisk.jpg
Source11:       PaineinClouds.jpg
Source12:       Peaks.jpg
Source13:       PurpleBrush.jpg
Source14:       Sand.jpg
Source15:       Sunrise.jpg
Source16:       Wind.jpg

Source21:       COPYING
Source22:       metadata.json

BuildArch:     noarch
BuildRequires: ImageMagick
Requires:      filotimo-kde-overrides


%description
Wallpapers for Filotimo.

%define debug_package %{nil}

%prep

%build

%install
install -pm 0644 %{SOURCE0} LICENSE

cd %{_topdir}

sed -i 's/"@author_name@"/"Marek Piwnicki"/' metadata.json
sed -i 's/"@author_email@"/"marpiwnicki@gmail.com"/' metadata.json

for file in $(ls | grep .jpg); do
    id=$(echo $file | cut -d '.' -f 1)

    mkdir -p %{buildroot}%{_datadir}/wallpapers/$id/contents/images
    cp $file %{buildroot}%{_datadir}/wallpapers/$id/contents/screenshot.jpg
    cp $file %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).jpg
    magick %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).jpg %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).png
    rm -f %{buildroot}%{_datadir}/wallpapers/$id/contents/images/$(identify -format "%wx%h\n" $file).jpg
    cp metadata.json %{buildroot}%{_datadir}/wallpapers/$id/
    cp %{SOURCE21} %{buildroot}%{_datadir}/wallpapers/$id/

    sed -i 's/"@id@"/\"'"$id"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json

    name=""
    case "$id" in
        "ColdDunes") name="Cold Dunes"
        ;;
        "FirstSnow") name="First Snow"
        ;;
        "HillsandMountains") name="Hills and Mountains"
        ;;
        "InClouds") name="In Clouds"
        ;;
        "MountainLanterns") name="Mountain Lanterns"
        ;;
        "PaineinClouds") name="Paine in Clouds"
        ;;
        "PinkHat") name="Mont Blanc's Pink Hat"
        ;;
        "PurpleBrush") name="Purple Brush"
        ;;
        *) name=$id
        ;;
    esac
    sed -i 's/"@name@"/\"'"$name"'\"/' %{buildroot}%{_datadir}/wallpapers/$id/metadata.json
done


%files
%license LICENSE
%{_datadir}/wallpapers/*

%changelog
