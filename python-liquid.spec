# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define shortname liquid

Name:           python-liquid
Version:        0.0.1
Release:        1%{?dist}
Summary:        A small web framework written in python using dependency injection technology.

Group:          Development/Languages
License:        Apache
URL:            http://liquid.refnode.com/
Source0:        https://refnode.com/refnode/liquid/archive/v%{release}.tar.gz

#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python-setuptools

%description
Reimplementation of the ruby liquid template lib.


%prep
%setup -q
#%setup -q -n %{shortname}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
#rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md LICENSE ChangeLog
%{python_sitelib}/%{shortname}/
%dir %{python_sitelib}/%{shortname}-%{version}-*.egg-info
%{python_sitelib}/%{shortname}-%{version}-*.pth


%changelog
