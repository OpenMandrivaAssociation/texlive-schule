# revision 34107
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-schule
Version:	20140620
Release:	4
Summary:	TeXLive schule package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schule.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schule.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schule.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive schule package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/schule/relaycircuit.sty
%{_texmfdistdir}/tex/latex/schule/schule.sty
%{_texmfdistdir}/tex/latex/schule/schuleab.cls
%{_texmfdistdir}/tex/latex/schule/schulein.cls
%{_texmfdistdir}/tex/latex/schule/schuleit.cls
%{_texmfdistdir}/tex/latex/schule/schulekl.cls
%{_texmfdistdir}/tex/latex/schule/schulekl.sty
%{_texmfdistdir}/tex/latex/schule/schuleub.cls
%{_texmfdistdir}/tex/latex/schule/schuleue.cls
%{_texmfdistdir}/tex/latex/schule/schulinf.sty
%{_texmfdistdir}/tex/latex/schule/schullsg.cls
%{_texmfdistdir}/tex/latex/schule/schullzk.cls
%{_texmfdistdir}/tex/latex/schule/schullzk.sty
%{_texmfdistdir}/tex/latex/schule/schulphy.sty
%{_texmfdistdir}/tex/latex/schule/syntaxdi.sty
%doc %{_texmfdistdir}/doc/latex/schule/README
%doc %{_texmfdistdir}/doc/latex/schule/schule.pdf
#- source
%doc %{_texmfdistdir}/source/latex/schule/schule.dtx
%doc %{_texmfdistdir}/source/latex/schule/schule.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
