Name:		texlive-schule
Version:	0.6
Release:	2
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
%{_texmfdistdir}/tex/latex/schule
%doc %{_texmfdistdir}/doc/latex/schule
#- source
%doc %{_texmfdistdir}/source/latex/schule

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
